# -*- coding: utf-8 -*-
import datetime
import re
import random
import json
from termcolor import colored
from urllib.request import urlopen
from bs4 import BeautifulSoup

from db import *

random.seed(datetime.datetime.now())
# Получение стартовой ссылки
def getLinks(articleUrl):
    html = urlopen('https://en.wikipedia.org' + articleUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    return bsObj.find('div', {'id':'bodyContent'}).findAll('a', href = re.compile('^(/wiki/)((?!:).)*$'))

# Открытие и поиск всех IP адресов
def getHistoryIPs(pageUrl):
    pageUrl = pageUrl.replace('/wiki/', '')
    historyUrl = f'https://en.wikipedia.org/w/index.php?title={pageUrl}&action=history'
    print(colored('History url is:', 'yellow'), (f'{historyUrl}'))
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    #Выборка ip адресов и запись их в set()
    ipAddresses = bsObj.findAll("a", {"class":"mw-anonuserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        if ipAddress not in addressList:
            addressList.add(ipAddress.get_text())
    return addressList

# Получение местонахождения через переданный IP адрес
def getCountry(ipAddress):
    from urllib.error import URLError, HTTPError
    while (len(ip) > 0 and len(ip) < 15):
        try:
            response = urlopen(f'http://api.ipstack.com/{ipAddress}?access_key=08416ca257096ff79667a183ab8cec70').read().decode()
        except HTTPError:
            return None
        responseJson = json.loads(response)
        return responseJson.get('country_name')


if __name__ == '__main__':
    links = getLinks('/wiki/Uffizi')
    while (len(links) > 0):
        try:
            for link in links:
                historyIPs = getHistoryIPs(link.attrs['href'])
                for ip in historyIPs:
                    country = getCountry(ip)
                    if len(ip) < 15:
                        INSERT_DB(ip, country)
                        print(colored(ip, 'green'), ('- is from'), colored(country, 'magenta'))
                print('')
        except Exception as e:
            print(colored(" ERROR:", 'red'), (str(e)))
            continue
        except KeyboardInterrupt:
            print('\nBye')
            break
        finally:
            cur.close()
            conn.close()
        newLink = links[random.randint(0, len(links)-1)].attrs['href']
        links = getLinks(newLink)
