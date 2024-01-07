#!/usr/bin/python3
"""email address, sends a POST request to the passed URL"""
import requests
from sys import argv


if __name__ == "__main__":

    email = {'email': argv[2]}
    r = requests.post(argv[1], data=email)

    print("Your email is: {}".format(r.text)
