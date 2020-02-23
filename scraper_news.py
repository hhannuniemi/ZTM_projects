#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scraping links from hacker news using Beautiful Soup

@author: hannahannuniemi
"""
import requests
from bs4 import BeautifulSoup
import pprint

urls = ['https://news.ycombinator.com/news', 'https://news.ycombinator.com/news?p=2']
def get_links(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.storylink')
    subtext = soup.select('.subtext')
    return links, subtext


def sort_by_scores(news_list):
    return sorted(news_list, key= lambda k: k['scores'], reverse=True)


def custom_news(links, subtext):
    news = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        score = subtext[idx].select('.score')
        if len(score):
            points = int(score[0].getText().replace(' points', ''))
            print(points)
            if points > 99:
                news.append({'title': title, 'link': href, 'scores': points})
    return sort_by_scores(news)

l1, s1 = get_links(urls[0])
l2, s2 = get_links(urls[1])
links = l1 + l2
subtext = s1 + s2
        
pprint.pprint(custom_news(links, subtext))