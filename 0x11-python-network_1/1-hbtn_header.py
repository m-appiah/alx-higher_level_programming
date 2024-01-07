#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found in the header"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
