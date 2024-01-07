#!/usr/bin/python3
"""email address, sends a POST request to the passed URL"""
import requests
from sys import argv


if __name__ == "__main__":

    payload = {'email': argv[2]}
    response = requests.post(argv[1], data=payload)

    print(f"Your email is: {response.text}")
