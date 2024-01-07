#!/usr/bin/python3
"""email address, sends a POST request to the passed URL"""
import requests
import sys


if __name__ == "__main__":

    email = {'email':sys.argv[2]}
    r = requests.post(sys.argv[1], data=email)

    print("Your email is: {}".format(r.text)
