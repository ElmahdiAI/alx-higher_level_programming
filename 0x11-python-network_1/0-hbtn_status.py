#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status using urllib"""

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read().decode('utf-8')
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
