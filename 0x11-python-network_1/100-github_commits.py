#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails”
"""
import sys
import requests


if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(
            owner_name, repository_name)
    pars = {"per_page": 10}

    response = requests.get(url, pars=pars)
    commits = response.json()
    try:
        for commit in commits:
            sha = commit.get("sha")
            author_name = commit.get("commit").get("author").get("name")
            print("{}: {}".format(sha, author_name))
    except IndexError:
        pass
