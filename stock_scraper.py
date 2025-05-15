# FILE NAME - stocks.py

# NAME - Oliver Doty
# DATE - 5/10/2025
# DESCRIPTION - This code grabs the requested stock and displays its price


import requests
from bs4 import BeautifulSoup

scrape_address = input("Enter a stock symbol: ")
page = requests.get(f'https://phishingdemo.org/python/scraping/{scrape_address}.html', headers={"User-Agent": ""})
#print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')

price = soup.find(id="price").string
print(price)