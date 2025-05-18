# FILE NAME - maze.py

# NAME - Oliver Doty
# DATE - 
# DESCRIPTION - 


import requests
from bs4 import BeautifulSoup


maze_address = input("Enter the starting page: ")

new_page = maze_address + ".html" 
while True:
    page = requests.get(f'https://phishingdemo.org/python/scraping/maze/{new_page}', headers={"User-Agent": ""})
    soup = BeautifulSoup(page.content, 'html.parser')
    new_page = str(soup)
    soup_str = soup_str[17:-15]
    print(new_page)
    if len(new_page) <= 9:
        print(new_page)
        break




#soup_str = str(soup)

#page2 = requests.get(f'https://phishingdemo.org/python/scraping/maze/{soup_str}', headers={"User-Agent": ""})
#soup = BeautifulSoup(page2.content, 'html.parser')

#if len(soup_str) >= 4:
#    soup_str = str(soup)
#
#    page2 = requests.get(f'https://phishingdemo.org/python/scraping/maze/{soup_str}', headers={"User-Agent": ""})
#    soup = BeautifulSoup(page2.content, 'html.parser')
#    print(soup_str)
#else:
#    print(soup_str)
#print(soup_str)
#print(soup)