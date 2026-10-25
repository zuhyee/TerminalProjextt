import os
from github import Github, GithubException

TOKEN = os.environ.get("PR_TOKEN")
REPO_NAME = "zuhyee/TerminalProjextt"

if not TOKEN:
    raise SystemExit("PR_TOKEN not found. Check your Codespaces secret.")

try:
    github = Github(TOKEN)
    repo = github.get_repo(REPO_NAME)

    print(f"Connected to {repo.full_name}!")

    base = input("Target branch (usually main): ").strip()
    head = input("Source branch: ").strip()
    title = input("PR title: ").strip()
    body = input("PR description: ").strip()

    pr = repo.create_pull(
        title=title,
        body=body,
        head=head,
        base=base
    )

    print(f"\nPR CREATED! {pr.html_url}")

except GithubException as error:
    print(f"GitHub error: {error.status}")
    print(error.data.get("message", "Unknown error"))
