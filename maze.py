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
    soup = soup.body
    new_page = str(soup)

    if len(new_page) <= 15:
        print(new_page)
        break
    new_page = new_page[12:-7]
    print(new_page)



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