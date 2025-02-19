import re
import requests
import json
import pytz
import tzlocal
from datetime import datetime
from rich.console import Console
from collections import defaultdict
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from functools import lru_cache

console = Console()

GITHUB_API_URL = "https://api.github.com/users/{}/events"

@lru_cache(maxsize=10) # Store up to 10 user's recent activity
def fetch_github_activity(username):
    """
    Fetch and cache recent activity of a GitHub user.
    """
    api_url = GITHUB_API_URL.format(username)

    # Handle API response errors
    try:
        with Progress(
            SpinnerColumn(),  # Spinning loader
            BarColumn(),  # Progress bar
            TextColumn("[cyan]Fetching data...[/]"),
            transient=True  # Removes progress bar after completion
        ) as progress:
            task = progress.add_task("", total=1)

            response = requests.get(api_url, timeout=10) # Set a timeout to prevent hanging
            response.raise_for_status() # Raises HTTPError for bad responses

        try:
            data = response.json()
            progress.update(task, completed=1)  # Marks progress as complete

        except json.JSONDecodeError:
            console.print("[red]❌ Error:[/] failed to decode JSON response.")
            return 

        if not data:
            console.print(f"[yellow]No recent activity found for this user.[/]")
            return
        console.print("[green]✅ Fetch complete![/]")
        return data

    except requests.exceptions.ConnectionError:
        console.print("[bold red]❌ Error:[/] No internet connection. Please check your network.")
    except requests.exceptions.Timeout:
        console.print("[bold red]❌ Error :[/]: Request timed out. GitHub API might be slow. Try again later.")
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            console.print(f"[bold red]❌ Error {response.status_code}:[/] GitHub user not found.")
        elif response.status_code == 403:
            console.print(f"[yellow]⚠️ Error {response.status_code}:[/] API rate limit exceeded. Try again later")
        else:
            console.print(f"[bold red]❌ Unexepecetd error:[/] {response.status_code} - {http_err}")
    except requests.exceptions.RequestException as req_err:
        console.print(f"[bold red]❌ Network Error:[/] {req_err}")
    except Exception as err:
        console.print(f"[bold red]❌ An unexpected error occurred:[/] {err}")

def display_github_activity(username, events, filter_type = None):
    """
    Format GitHub activity events.
    """
    push_events = defaultdict(int) # To push commits per repo
    messages = []

    print(f"\n📌 Recent Activity for {username.lower()}")
    print("-"*70)

    try:
        dt_obj= datetime.strptime(events[0]["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        utc_time = pytz.utc.localize(dt_obj)
        local_timezone = tzlocal.get_localzone()
        local_time = utc_time.astimezone(local_timezone)
        last_active = local_time.strftime("%d %b %Y, %H:%M %Z")

        for event in events:
            event_type = event.get("type", "UnknownEvent")
            repo_name = event.get("repo", {}).get("name", "UnknownRepo")

            if filter_type  and event_type != filter_type: 
                continue

            if event_type == "PushEvent":
                commit_count = event.get("payload", {}).get("size", 0)
                push_events[repo_name] += commit_count
            elif event_type == "IssuesEvent":
                messages.append(f"🛠  Opened a new issue to {repo_name}")
            elif event_type == "WatchEvent":
                messages.append(f"⭐ Starred {repo_name}")
            elif event_type == "ForkEvent":
                messages.append(f"🍴 Forked {repo_name}")
            elif event_type == "PullRequestEvent":
                messages.append(f"🔃 Opened a pull request to {repo_name}")
            
    except Exception as e:
        messages.append(f"[bold red]❌ Error processing an event: {str(e)}[/]")

    for repo, total_commits in push_events.items():
        commit_text = "commit" if total_commits == 1 else "commits"
        messages.append(f" ⬆ Pushed {total_commits} {commit_text} to {repo}")

    return last_active, messages

def main():
    """
    CLI loop for user input handling
    """
    print("🔹 Welcome to GitHub User Activity CLI")
    print("🔹 Usage: github-activity <username>")
    print("🔹 Type 'help' for commands, 'exit' to quit \n")

    while True:
        command = input("cli> ").strip()

        if command.lower() == "exit":
            confirm = input("Are you sure you want to exit? (y/n): ").strip().lower()
            if confirm == "y":
                break
            continue

        if command.lower() == "help":
            print("\nAvailable Commands:")
            print(" github-activity <username>                        →  Fetch GitHub acivity")
            print(" github-activity <username> <optional:event-type>  →  Fetch and filter GitHub acivity by event type")
            print(" clear-cache                                       →  Clear cached data")
            print(" exit                                              →  Exit CLI")
            continue

        if command.lower() == "clear-cache":
            fetch_github_activity.cache_clear()
            print("🧹 Cache cleared!")
            continue

        # Regex pattern to extract username
        user_activity_pattern = r'^github-activity\s+(\S+)(?:\s+(\S+))?$'
        match = re.match(user_activity_pattern, command, re.IGNORECASE)

        if match:
            username = match.group(1).strip()
            event_type = match.group(2).strip() if match.group(2) else None
            user_events = fetch_github_activity(username)
            
            if user_events != None:
                last_seen, activities = display_github_activity(username,user_events, event_type)
                console.print(f"[yellow]Last active on {last_seen}\n[/]")
                for activity in activities:
                    console.print(activity)
        else:
            console.print("[bold red]❌ Invalid command.[/] Use 'help' for list of commands.")

if __name__ == "__main__":
    main()
 