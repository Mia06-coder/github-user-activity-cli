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
Command	                            → Description
github-activity <username>	    → Fetch GitHub activity of a user.
help	                            → Show available commands.
exit	                            → Quit the CLI.
```

### Example:

```sh
cli> github-activity octocat
🔍 Fetching activity for GitHub user: octocat...
✅ Fetch complete!
```

## Dependencies

- **requests** → Handles HTTP requests to the GitHub API
- **rich** → Provides colored output and a progress ba

To install them manually:

```sh
pip install requests rich
```

## Error Handling 🛠

- ❌ No internet connection → Error: No internet connection.
- ❌ Invalid username → Error: GitHub user not found.
- ⚠️ Rate limit exceeded → API rate limit exceeded. Try again later.

## Contributing 🤝

Feel free to open issues and submit pull requests to improve the project! 🎉
