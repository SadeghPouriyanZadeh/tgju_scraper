import requests
from bs4 import BeautifulSoup


def scrap(target):
    headers = headers = {
        "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"""
    }

    url = r"https://www.tgju.org/"
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    prices = [div.text for div in soup.find_all("span", class_="info-price")]
    if target == "gold_18":
        return prices[3]
    elif target == "gold_coin":
        return prices[3]
    elif target == "tether":
        return prices[3]
    elif target == "bitcoin":
        return prices[3]
    else:
        raise "use one of these as target: gold_18,gold_coin,tether,bitcoin"
