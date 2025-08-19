# scanzaclip Bootstrap

This package was generated to help you spin up 7 repos with CI/CD quickly.

## Quick start

1) Set environment variables (Linux/macOS):
```bash
export GITHUB_USER="your_github_username"
export GITHUB_TOKEN="ghp_..."        # token with `repo` scope
export REPLIT_TOKEN="your_replit_token"   # optional
export SCANNERC_API_KEY="replace_me"      # optional
```

Windows (PowerShell):
```powershell
setx GITHUB_USER "your_github_username"
setx GITHUB_TOKEN "ghp_..."
setx REPLIT_TOKEN "your_replit_token"
setx SCANNERC_API_KEY "replace_me"
```

2) Run the orchestrator (creates the 7 repos on GitHub, pushes code, sets CI):
```bash
python bootstrap_create_and_push.py
```

3) (Optional) Create Replit projects from each repo (requires `repl` CLI and login):
```bash
bash replit_deploy.sh
```

---
