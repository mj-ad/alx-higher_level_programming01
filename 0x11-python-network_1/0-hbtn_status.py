#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
from urllib.request import Request, urlopen
if __name__ == '__main__':
    req = Request('https://alx-intranet.hbtn.io/status')
    with urlopen(req) as response:
        body = response.read()
        print('Body response:$')
        print('\t- type: ', type(body))
        print('\t- content: ', body)
        print('\t- utf8 content: ', body.decode('utf8'))
