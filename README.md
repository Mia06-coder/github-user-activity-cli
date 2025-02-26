# GitHub User Activity CLI 🚀

A simple command-line tool to fetch and display the **recent activity** of any GitHub user using the GitHub API.  
Built with **Python** and features robust **error handling** and a **user-friendly CLI**.

## Features ✨

- Fetch recent GitHub activity by username.
- Handles **network errors**, **invalid users**, and **rate limits**.
- Interactive **CLI with commands** (`github-activity <username>`, `help`, `exit`).
- Status messages and error alerts for better user experience.
- Rich-formatted CLI with color output
- Progress bar while fetching data
- 📌 Supports:
  - Pushed commits (`PushEvent`)
  - Opened issues (`IssuesEvent`)
  - Starred repositories (`WatchEvent`)
  - Forked repositories (`ForkEvent`)
  - Opened pull requests (`PullRequestEvent`)
- Stores the latest data for up to 10 users to reduce API calls.
- Use `clear-cache` to refresh stored data.
- Allows filtering by event type (e.g., `PushEvent`, `PullRequestEvent`)

## Installation 🔧

Make sure you have **Python 3.7+** installed.

1. Clone the repository:

```sh
git clone https://github.com/mia06-coder/github-user-activity-cli.git
```

2. Navigate into the directory:

```sh
cd github-user-activity-cli
```

3. Install dependencies

```sh
pip install -r requirements.txt
```

## Usage 🚀

Run the script:

```sh
python useractivity.py
```

## CLI Commands:

```sh
Command	                                            Description
-------------------------------------------------------------------------
github-activity <username>	                    → Fetch GitHub activity of a user.
clear-cache                                         → Clear cached data.
github-activity <username> <optional:event-type>    → Fetch and filter GitHub acivity by event type
help	                                            → Show available commands.
exit	                                            → Quit the CLI.
```

### Example:

#### Fetch GitHub User Activity

```sh
cli> github-activity mbostock
⠏ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Fetching data...
```

```sh
cli> github-activity mbostock
✅ Fetch complete!

📌 Recent Activity for mbostock
----------------------------------------------------------------------
Last active on 20 Feb 2025, 22:12 SAST

💬 Commented on 2 issues to observablehq/plot
🔃 Opened 4 pull requests to observablehq/plot
⬆️  Pushed 5 commits to observablehq/plot
🗑 Deleted  2 branches to observablehq/plot
🛠 Opened  1 new issue to observablehq/plot
🔍 Reviewed 1 pull request to observablehq/plot
🔍 Reviewed 1 pull request to mbostock/isoformat
cli> github-activity mbostock pull
```

#### Fetch GitHub User Activity by event type

```sh
cli> github-activity mbostock  pull

📌 Recent Activity for mbostock
----------------------------------------------------------------------
Last active on 20 Feb 2025, 22:12 SAST

🔃 Opened 4 pull requests to observablehq/plot
🔍 Reviewed 1 pull request to observablehq/plot
🔍 Reviewed 1 pull request to mbostock/isoformat
```

#### Exit CLI

```sh
cli> exit
```

## Dependencies

- **requests** → Handles HTTP requests to the GitHub API
- **rich** → Provides colored output and a progress ba
- **tzlocal** → For dynamically detecting and using the local timezone.

To install them manually:

```sh
pip install requests rich tzlocal
```

## Error Handling 🛠

- ❌ No internet connection → Error: No internet connection.
- ❌ Invalid username → Error: GitHub user not found.
- ⚠️ Rate limit exceeded → API rate limit exceeded. Try again later.

## Contributing 🤝

Feel free to open issues and submit pull requests to improve the project! 🎉

## 🎨 Credits & Inspiration

This project idea was inspired by [roadmap.sh](https://roadmap.sh/projects/github-user-activity).  
Check it out for more project ideas and learning resources!
