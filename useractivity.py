import re
import requests
import json

GITHUB_API_URL = "https://api.github.com/users/{}/events"

def fetch_github_activity(username):
    """
    Fetch recent activity of a GitHub user.
    """
    api_url = GITHUB_API_URL.format(username)

    # handle API response errors
    try:
        response = requests.get(api_url, timeout=10) # Set a timeout to prevent hanging
        response.raise_for_status() # Raises HTTPError for bad responses

        try:
            data = response.json()

        except json.JSONDecodeError:
            print("❌ Error: failed to decode JSON response.")
            return 

        if not data:
            print(f"No recent activity found for this user.")
            return
        else:
            print("Data successfully fetched!")
            return

    except requests.exceptions.ConnectionError:
        print("❌ Error: No internet connection. Please check your network.")
    except requests.exceptions.Timeout:
        print("❌ Error: Request timed out. GitHub API might be slow. Try again later.")
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"❌ Error: GitHub user not found.")
        elif response.status_code == 403:
            print(f"⚠️ Error: API rate limit exceeded. Try again later")
        else:
            print(f"❌ Unexepecetd error: {response.status_code} - {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"❌ Network Error: {req_err}")
    except Exception as err:
        print(f"❌ An unexpected error occurred: {err}")

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
            print(" github-activity <username>  ->  Fetch GitHub acivity")
            print(" exit                        ->  Exit CLI")
            continue

        # Regex pattern to extract username
        user_activity_pattern = r'^github-activity\s+(\S+)$'
        match = re.match(user_activity_pattern, command, re.IGNORECASE)

        if match:
            username = match.group(1).strip()
            print(f"🔍 Fetching activity for GitHub user: {username}...")
            fetch_github_activity(username)

        else:
            print("❌ Invalid command. Use 'help' for list of commands.")

if __name__ == "__main__":
    main()
 