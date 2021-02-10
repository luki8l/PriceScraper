import requests
from bs4 import BeautifulSoup


# sg.Window(title="Price Sccraper", layout=[[]], margins=(100,50)).read()

URL = 'https://www.amazon.de/Nike-Chelsea-Pre-Match-Jersey-Concord/dp/B08KJGMCN2/ref=sr_1_1_sspa?dchild=1&keywords=chelsea+trikot&qid=1612952062&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNjlGUTdPVlMzVUhLJmVuY3J5cHRlZElkPUEwOTM2MDM1MkJWQURGSVQ0UUhRMSZlbmNyeXB0ZWRBZElkPUEwOTg0MDM0M0oyV1BaQ0hUU0MxVSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

URL=input("Paste your Amazon Link: \n")

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'

headers={
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}

page=requests.get(URL, headers=headers)

soup=BeautifulSoup(page.content, 'html.parser')

price = soup.find(id="priceblock_ourprice").getText()
price=float(price[:-2].replace(',','.'))

print(price)