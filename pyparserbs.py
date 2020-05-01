import requests
from bs4 import BeautifulSoup


# Collect and parse first page
page = requests.get('https://www.imdb.com/chart/top/')
soup = BeautifulSoup(page.text, 'html.parser')
artist_name_list = soup.find(class_='lister-list')
trs = artist_name_list.findAll('tr')
title = []
rating = []
for tr in trs:
    title.append(tr.find('td',{'class':'titleColumn'}))
    rating.append(tr.find('td',{'class':'ratingColumn imdbRating'}).text)
print(title)
