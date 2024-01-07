#!/usr/bin/python3
"""request to the URL and displays the body of the response in utf-8"""
import urllib.request
import urllib.error
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    try:
        with urllib.request.urlopen(url) as r:
            content = r.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
