#!/usr/bin/python3
"""
Python script that takes 2 arguments (repository and user) and gets the
last 10 commits
"""
import requests, sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    headers = {'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28'}
    r = requests.get(
            "https://api.github.com/repos/{}/{}/commits".format(
                repo_name, owner_name), headers=headers)
    commits = r.json()[:10]
    for commit in commits:
        print("{}: {}".format(
            commit.get("sha"),
            commit.get("commit").get("author").get("name")))
