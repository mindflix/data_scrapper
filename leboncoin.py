# -*- coding: utf-8 -*-
import requests as r
import bs4 as bs
from selenium import webdriver


class ChromeHandler:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
        }

    def open_url(self, url):
        


chromedriver = "./env/bin/chromedriver"

options = webdriver.ChromeOptions()
options.add_argument("window-size=1200x600")  # optional
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
)


browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

browser.implicitly_wait(0.5)

url = "https://www.leboncoin.fr/"
browser.get(url)

get_html = browser.page_source

print(get_html)


soup = bs.BeautifulSoup(html, "lxml")
result = str(soup.findAll("div", {"id": "recaptcha_image"}))
result = result.split('"')[11]


def main():
    print(result)


main()
