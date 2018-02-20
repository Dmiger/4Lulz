# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 18:13:09 2018

@author: Sony VAIO Pro
"""  

from bs4 import BeautifulSoup as bs
import requests
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


url = 'https://www.intimcity.nl/' # URL to scrape from


def getData(url):
    
    blyads = []
    i = 0 # Key to identify restaurants
    pages = range(1,81)   # Range of strings to add to URL to go to next result page
    
    for page in pages:
            time.sleep(0.1)
            url1 = url+str('persons.php?type=0&style=0&news=0&updated=0&video=N&t=&retouch=0&index=')+str(page)  # URL to search
            request = requests.get(url1)
            html = request.text
            soup = bs(html,"html.parser")
            results = soup.findAll('div', {"class" : "psnCrd2x"})
            
            
            for result in results:  
                blyads.append({})
                #Грузим адрес
                address = result.findAll('a', {"class" : "index"})
                try:
                    address = address[0].getText()
                    blyads[i]['metro'] = address
                except IndexError:
                    pass
                
                #Цены за час, два и за ночь           
                price_1 = result.findAll('span', {"class" : "p_p1"})
                price_2 = result.findAll('span', {"class" : "p_p2"})
                price_n = result.findAll('span', {"class" : "p_pn"})
                blyads[i]['chas'] = price_1[0].getText().replace('$','')
                blyads[i]['dva_chasa'] = price_2[0].getText().replace('$','')
                blyads[i]['noch'] = price_n[0].getText().replace('$','')
                #Возраст и размер
                age_sis = result.findAll('td', {"class" : "psnCrd7"})
                age_sis = age_sis[0].getText(strip=True, separator=",")
                splits = age_sis.split(',')
                blyads[i]['vozrast'] = splits[0]
                blyads[i]['razmer'] = splits[1]
                
                #Грузим вес и рост
                weight_height = result.findAll('td', {"class" : "psnCrd8"})
                weight_height = weight_height[0].getText(strip=True, separator=",")
                splits2 = weight_height.split(',')
                try:
                    blyads[i]['ves'] = splits2[0]
                    blyads[i]['rost'] = splits2[1]
                except IndexError:
                    blyads[i]['rost'] = splits2[0]
                    blyads[i]['ves'] = 'n/a'
                    
                
                #А Нальчик?
                analchik = result.findAll('td', {"class" : "psnCrd12"})
                blyads[i]['vpopu'] = analchik[0].getText()
                #Описание
                #about = result.findAll('div', {"class" : "psnCrd10"})
                #blyads[i]['opisanie'] = about[0].getText()
                
                i+=1
                
    with open('data_raw.csv', 'w', newline = '') as file1:
        fieldnames = ['metro','chas','dva_chasa','noch','ves', 'rost',
                      'vozrast','razmer','vpopu']
        writer = csv.DictWriter(file1, fieldnames=fieldnames)
        writer.writeheader()
        for x in blyads:
            writer.writerow(x)
    