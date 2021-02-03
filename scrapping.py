#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 02:07:26 2021

@author: nashe
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import time
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import csv

review_sites = ['inferential-statistical-analysis-python', 'understanding-visualization-data', 'inferential-statistical-analysis-python', 'fitting-statistical-models-data-python' ]
all_reviews = []
def get_data(review_site):  
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    r = requests.get('https://www.coursera.org/learn/{}/reviews'.format(review_site), headers=headers)#, proxies=proxies)
    content = r.content
    soup = BeautifulSoup(content)
    print(soup)

    alls = []
    for d in soup.findAll('div', attrs={'class':'top-review'}):

        top_review = d.find('p', attrs={'class':'top-review_comment'})
         
        if top_review is not None:
            alls.append(top_review)
            
        print(top_review)
        

    for d in soup.findAll('div', attrs={'class':'reviewText'}):
        review = d.find('p')
        
        if review is not None:
            alls.append(review)
             
    
    return alls

for review_site in review_sites:
    all_reviews.append(get_data(review_site))

flatten = lambda l: [item for sublist in l for item in sublist]

with open('coursera_reviews.csv', mode='w') as coursera_reviews:
    writer = csv.writer(coursera_reviews, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    for review in flatten(all_reviews):
        writer.writerow(review)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#df = pd.DataFrame(flatten(all_reviews))
#df.to_csv('coursera_reviews.csv', index=False, encoding='utf-8')