#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 02:07:26 2021

@author: nashe
"""

from bs4 import BeautifulSoup
import requests
import csv

review_sites = ['inferential-statistical-analysis-python', 'understanding-visualization-data', 'fitting-statistical'
                                                                                               '-models-data-python']
all_reviews = []
all_ratings = []


def get_data(review_site):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
               "Accept-Encoding": "gzip, deflate",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
               "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    r = requests.get('https://www.coursera.org/learn/{}/reviews'.format(review_site),
                     headers=headers)  # , proxies=proxies)
    content = r.content
    soup = BeautifulSoup(content)

    all_reviews = []
    all_stars = []

    for d in soup.findAll('div', attrs={'class': 'top-review'}):
        top = 0
        for d_review in d.find('div', attrs={'class': '_1mzojlvw'}):
            full_star = d_review.find('svg', attrs={'class': '_ufjrdd',
                                                    'style': 'fill:#F7BB56;height:14px;width:14px;margin-right:2px;vertical-align:text-bottom'})
            if len(str(full_star)) == 518:
                top = top + 1

        all_stars.append(top)

        top_review = d.find('p', attrs={'class': 'top-review_comment'})
        if top_review is not None:
            all_reviews.append(top_review)

    for d in soup.findAll('div', attrs={'class': 'reviewText'}):
        review = d.find('p')

        if review is not None:
            all_reviews.append(review)

    for d_review_bottom in soup.findAll('div', attrs={'class': '_jyhj5r review review-page-review m-b-2'}):
        bottom = 0
        for d_bottom_review in d_review_bottom.find('div', attrs={'class': '_1mzojlvw'}):
            bottom_full_star = d_bottom_review.find('svg', attrs={'class': '_ufjrdd',
                                                                  'style': 'fill:#F7BB56;height:14px;width:14px'
                                                                           ';margin-right:2px;vertical-align:text'
                                                                           '-bottom'})
            # print(bottom_full_star)
            if bottom_full_star is not None:
                bottom = bottom + 1

        all_stars.append(bottom)

    return all_reviews, all_stars


for review_site in review_sites:
    temp_reviews, temp_ratings = get_data(review_site)
    all_reviews.append(temp_reviews)
    all_ratings.append(temp_ratings)

flatten = lambda l: [item for sublist in l for item in sublist]

with open('coursera_reviews.csv', mode='w') as coursera_reviews:
    writer = csv.writer(coursera_reviews, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for review in flatten(all_reviews):
        print(review)
        writer.writerow(review)

with open('coursera_review_rating.csv', mode='w') as coursera_review_ratings:
    writer = csv.writer(coursera_review_ratings, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    all_ratings_flattened = list(flatten(all_ratings))

    for rating in all_ratings_flattened:
        writer.writerow(str(rating))
        print(rating)

