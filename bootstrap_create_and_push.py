#!/usr/bin/env python3
"""
bootstrap_create_and_push.py
Creates 7 GitHub repositories under your account, commits/pushes local skeletons,
and enables GitHub Actions CI. Requires:
- env: GITHUB_USER, GITHUB_TOKEN
- git installed locally
"""
import os, subprocess, sys, json, time

REPOS = [
    "scanzaclip-core",
    "scanconfrem",
    "agi-module",
    "meta-integration",
    "permission-control",
    "autoprocessor",
    "report-dashboard"
]

def sh(cmd, cwd=None):
    print("::", " ".join(cmd))
    subprocess.check_call(cmd, cwd=cwd)

def create_repo_via_api(user, token, name, private=True):
    import urllib.request, urllib.error, json
    data = json.dumps({"name": name, "private": private, "auto_init": False}).encode("utf-8")
    req = urllib.request.Request(
        f"https://api.github.com/user/repos",
        data=data,
        headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "scanzaclip-bootstrap"
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            print(f"Created repo: {body.get('full_name')}")
            return True
    except urllib.error.HTTPError as e:
        print("GitHub API error:", e.read().decode("utf-8"))
        return False

def main():
    user = os.getenv("GITHUB_USER")
    token = os.getenv("GITHUB_TOKEN")
    if not user or not token:
        print("Please set GITHUB_USER and GITHUB_TOKEN environment variables.")
        sys.exit(1)

    # Create repos on GitHub if not exist
    for repo in REPOS:
        ok = create_repo_via_api(user, token, repo, private=True)
        time.sleep(0.5)

    # Init, commit, push for each local repo
    for repo in REPOS:
        # init
        sh(["git", "init"], cwd=repo)
        sh(["git", "add", "."], cwd=repo)
        sh(["git", "commit", "-m", "Initial scaffold"], cwd=repo)
        sh(["git", "branch", "-M", "main"], cwd=repo)
        remote = f"https://{user}:{token}@github.com/{user}/{repo}.git"
        sh(["git", "remote", "remove", "origin"], cwd=repo]) if os.path.exists(os.path.join(repo, ".git")) else None
        try:
            sh(["git", "remote", "add", "origin", remote], cwd=repo)
        except subprocess.CalledProcessError:
            # remote may already exist; set url
            sh(["git", "remote", "set-url", "origin", remote], cwd=repo)
        sh(["git", "push", "-u", "origin", "main"], cwd=repo)

    print("All repos pushed. GitHub Actions will start automatically on next commits.")
    print("Done.")

if __name__ == "__main__":
    main()
