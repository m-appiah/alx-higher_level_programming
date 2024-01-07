#!/usr/bin/python3
"""email address, sends a POST request to the passed URL"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}

    r = requests.post(url, data=email)
    print(r.text)
