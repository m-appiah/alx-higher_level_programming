#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails”
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    response = requests.get(url)
    commits = response.json()
    try:
        for commit in range(10):
            print("{}: {}".format(
                commits[i].get("sha"), commits[i].gt(
                    "commit").get("author").get("name")))
    except IndexError:
        pass
