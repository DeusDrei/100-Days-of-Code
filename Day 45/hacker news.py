from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_page = response.text

soup = BeautifulSoup(yc_page, "html.parser")

websites = soup.select("span.titleline > a")

counter = 0
for i in websites:
    counter += 1
    j = i.get("href")
    print(f"{counter}. {i.text}\n Link: {j}")




