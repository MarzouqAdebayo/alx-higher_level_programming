#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = url.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        res = response.read().decode('utf-8')
