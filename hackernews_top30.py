import requests
import json
from bs4 import BeautifulSoup

hacker_news_url = "https://news.ycombinator.com/news"
title_list = []

response = requests.get(hacker_news_url)
print(response.status_code) #to check my status

soup = BeautifulSoup(response.text, "html.parser")

title_link = soup.find_all("span", class_="titleline")
for titles in title_link:
    title = titles.text  # Get the title text
    print(f"title: {title} ")
