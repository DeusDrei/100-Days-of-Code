import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
top_movies = response.text

soup = BeautifulSoup(top_movies, "html.parser")

movies = soup.select("h3.title")
sorted_movies = [i.text for i in movies[::-1]]

with open("movies.txt", "w", encoding="utf-8") as f:
    for i in sorted_movies:
        f.write(f"{i}\n")




