import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(URL)
contents = response.text


soup = BeautifulSoup(contents, "html.parser")
movie_list = []
titles = soup.find_all(name="h3", class_="title")
for movie in titles:
    name_of_movie = movie.getText()
    movie_list.append(name_of_movie)

movie_list.reverse()
print(movie_list)

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movie_list:
        file.write(f"{movie} \n")
