#!/usr/bin/env bash
# replit_deploy.sh
# Create Replit projects for all repos (requires `repl` CLI and login).
set -e
REPOS=(
  "scanzaclip-core"
  "scanconfrem"
  "agi-module"
  "meta-integration"
  "permission-control"
  "autoprocessor"
  "report-dashboard"
)
for repo in "${REPOS[@]}"; do
  echo "Creating/Updating Replit project for $repo"
  repl init "$repo" || true
done
echo "Done."
