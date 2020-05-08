import requests
from bs4 import BeautifulSoup
import class_csv


class bs:

    def __init__(self):
        return None
    
    def request_site_parse(self,site = 'https://www.imdb.com/chart/top/'):
        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')
        return soup

    def find_class(self,parse_data,class_name = 'lister-list'):
        return parse_data.find(class_=class_name)
        

# Collect and parse first page

x = bs()
y = class_csv.excel('Film')
sp = x.request_site_parse()
artist_name_list = x.find_class(sp,'lister-list')
trs = artist_name_list.findAll('tr')
title = []
rating = []
for tr in trs:
    title.append((tr.find('td',{'class':'titleColumn'}).text).replace("\n", "").strip())
    rating.append(tr.find('td',{'class':'ratingColumn imdbRating'}).text)
for i in range (0,len(title)):
    data = title[i] + rating[i]
    y.write_data(data)
