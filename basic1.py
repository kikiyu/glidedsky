#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    url = 'http://glidedsky.com/login'
 
    h = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    }

    # Get token of the login page.
    session = requests.session()
    # session.headers = h
    page = session.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    token = soup.find("input", {"name": "_token"})["value"]

    # Login
    data = {
        "_token": token,
        "email": "",
        "password": "",
    }
    res = session.post(url, data=data,)

    # Get the targe page with the session
    page = session.get('http://glidedsky.com/level/web/crawler-basic-1')
    # print(page.text)
    soup = BeautifulSoup(page.content, "html.parser")

    mydivs = soup.findAll('div', {'class': 'col-md-1'})
    sum = 0
    for div in mydivs:
        sum += int(div.text)
    print(sum)
