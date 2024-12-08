import requests
import json
from bs4 import BeautifulSoup

hacker_news_url = "https://news.ycombinator.com/news"

response = requests.get(hacker_news_url)
print(response.status_code) #to check my status
soup = BeautifulSoup(response.text, "html.parser")


news_title_and_url = soup.find_all("span", class_="titleline")
for titles in news_title_and_url:
    title = titles.a.text # Get the title text
    url = titles.a.get("href")
    print(f"title: {title}\nurl: {url}")
