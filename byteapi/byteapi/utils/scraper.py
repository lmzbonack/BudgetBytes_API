from bs4 import BeautifulSoup
import requests
import re

recipe_index = requests.get('https://www.budgetbytes.com/category/recipes/')

soup = BeautifulSoup(recipe_index.content, 'html.parser')

recipe_archives = soup.find('div', class_='archives').children

oh_places_to_go = []

for recipe in recipe_archives:
    for a in recipe.find_all('a', href=True):
        oh_places_to_go.append(a['href'])

# single = next(recipe_archives)
# print(single.prettify())

print(oh_places_to_go)

#Next grab the next page and continue scraping