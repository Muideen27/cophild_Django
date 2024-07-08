#!/bin/bash

# Find the root directory of the git repository
repo_root=$(git rev-parse --show-toplevel)

# Change to the root directory of the repository
cd "$repo_root" || exit

# Prompt for the file name
read -p "Enter the file name to add: $1" 

# Prompt for the commit message
read -p "Enter the commit message: $2"

# Add the file to the staging area
git add "$1"

# Commit the changes with the provided commit message
git commit -m "$2"

# Push the changes to the remote repository
git push

echo ""
echo "done"
