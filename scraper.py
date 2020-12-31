# Flipkart - Web Scraper using Python.
#
# @Author: Aditya Ambre
# @Date: 2020-12-27 19:11:45
# @Last Modified by:   Aditya Ambre
# @Last Modified time: 2020-12-30 16:55:20
#

import json
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
base_url = 'https://www.flipkart.com/search?q=mobile'

page_num = 1

id = 0

dt = []

while page_num <= 25:

    sleep(randint(2, 4))

    url = base_url + "&page=" + str(page_num)

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(response.status_code)

    for card in soup.findAll('div', {'class': '_13oc-S'}):
        for pr in card.findAll('a', {'class': '_2rpwqI'}):
            pd_link = pr.get('href')

            sleep(randint(1, 3))

            pd_url = 'https://www.flipkart.com' + pd_link

            r = requests.get(pd_url, headers=headers)
            soup = BeautifulSoup(r.text, 'html.parser')
            print(r.status_code)

            specs = ''

            for card in soup.findAll('div', {'class': '_1YokD2 _2GoDe3'}):
                for pr in card.findAll('span', {'class': 'B_NuCI'}):
                    title = pr.text
                for pr in card.findAll('div', {'class': '_30jeq3 _16Jk6d'}):
                    price = pr.text
                for pr in card.findAll('div', {'class': 'CXW8mj _3nMexc'}):
                    for prs in pr.findAll('img', src=True):
                        img = prs.get('src')
                for pr in card.findAll('div', {'class': '_2418kt'}):
                    specs = pr.text

                data = {}
                data['id'] = id
                data['page_num'] = page_num
                data['pd_url'] = pd_url
                data['title'] = title
                data['price'] = price
                data['img'] = img
                data['specs'] = specs

            id += 1

            dt.append(data)

    f = open('mobiles.json', 'w')
    f.write(json.dumps(dt))
    f.close()

page_num += 1

# Copyrights © - 2020 Aditya Ambre. │ All Rights Reserved.

# Description:
# This is a Flipkart Web-Scraper made using Python.
# 'requests' & 'BeautifulSoup4' python libraries are used in this Scraper.

# NOTE:
# Web Scraping can be used for collecting huge amounts of data for Analytics/Research purposes!
# Before scraping any website just ensure that you're not violating any of the Rules/Limitations mentioned in the '/robots.txt' of that particular website.
# The 'class' attributes can vary over the time, you may need to ensure them, if the scraper fails to run as intended! & Different websites have their own variable 'class'attributes.
# Tip: Try to Implement a 'Sleeper' within your 'Scraper' to reduce the Frequency of the 'no. of requests' sent to the remote server in the given amount of time while running the Scraper!
