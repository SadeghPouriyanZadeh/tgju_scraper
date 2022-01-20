import requests
from bs4 import BeautifulSoup
import time


class Tgju:
    def __init__(self):
        self.headers = {
            "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"""
        }
        self.url = r"https://www.tgju.org/"
        self.response = requests.get(url=self.url, headers=self.headers)
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        self.prices = [
            div.text for div in self.soup.find_all("span", class_="info-price")
        ]
        self.fetch_time = time.time()

    def get_gold_18(self):
        return int(self.prices[3].replace(",", ""))

    def get_gold_coin(self):
        return int(self.prices[4].replace(",", ""))

    def get_tether(self):
        return int(self.prices[7].replace(",", ""))

    def get_bitcoin(self):
        return int(self.prices[8].replace(",", ""))
