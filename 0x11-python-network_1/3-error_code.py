#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""
from urllib import request, error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = request.Request(url)

    try:
        with request.urlopen(req) as response:
            res = response.read().decode('ascii')
            print(res)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
