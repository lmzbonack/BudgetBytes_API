import requests
import time

from bs4 import BeautifulSoup

from recipes.models import Recipe

class BudgetByteScraper:
    """
    Scrapes recipe data from budgetbytes.com and loads it into app database
    """

    def __init__(self):
        self.recipe_list = []
        self.count = 0

    def populate_recipe_list(self):
        recipe_index = requests.get('https://www.budgetbytes.com/category/recipes/page/2/')
        soup = BeautifulSoup(recipe_index.content, 'html.parser')
        recipe_archives = soup.find('div', class_='archives').children

        # Get all recipe links on the page and save them in list
        for recipe in recipe_archives:
            for a in recipe.find_all('a', href=True):
                self.recipe_list.append(a['href'])

        # Grab the next page if it exists
        next_page_url = soup.find('a', class_='next', href=True)['href']

        while(True):
            next_recipe_page = requests.get(next_page_url)
            inside_soup = BeautifulSoup(next_recipe_page.content, 'html.parser')

            recipe_archives = inside_soup.find('div', class_='archives').children

            # Get all recipe links on the page and save them in list
            for recipe in recipe_archives:
                for a in recipe.find_all('a', href=True):
                    self.recipe_list.append(a['href'])

            next_page_url = inside_soup.find('a', class_='next', href=True)
            if(next_page_url == None):
                break
            next_page_url = next_page_url['href']
            self.count += 1

    def export_recipe_to_app(self, recipe_url):
        recipe_page =requests.get(recipe_url)
        soup = BeautifulSoup(recipe_page.content, 'html.parser')

        name = soup.find('h2', class_='wprm-recipe-name')
        
        ingredients_area = soup.find('ul', class_='wprm-recipe-ingredients')

        # If there is not an ingredients_area it is not a recipe
        if ingredients_area == None: return

        ingredients_list = [] 
        for ingredient in ingredients_area:
            ingredients_list.append(ingredient.text)

        instructions_area = soup.find('ul', class_='wprm-recipe-instructions')
        instructions_list = []
        for instructions in instructions_area:
            instructions_list.append(instructions.text)
        
        times = soup.find_all('span', class_='wprm-recipe-time')

        # If times does not have more than 2 entries it is not actually a recipe
        if len(times) < 2: return

        image = soup.find('img', class_='attachment-200x200')
        author = soup.find('span', class_='wprm-recipe-author')
        keywords = soup.find('span', class_='wprm-recipe-keyword')

        # Handle case of some recipes not having keywords
        if keywords == None: 
            keywords_django = ''
        else:
            keywords_django = keywords.text

        # Handle case of some recipes not having an author
        if author == None:
            author_django = ''
        else:
            author_django = author.text
        
        if 'data-lazy-src' in image:
            image_url_django = image['data-lazy-src']
        else:
            image_url_django = None

        Recipe.objects.get_or_create(
            name=name.text,
            ingredients=':'.join(ingredients_list),
            instructions=':'.join(instructions_list),
            prep_time=times[0].text,
            cook_time=times[1].text,
            image_url=image_url_django,
            keywords=keywords_django,
            author=author_django,
        )

        # id = 'some identifier'
        # person, created = Person.objects.get_or_create(identifier=id)

        # if created:
        #    # means you have created a new person
        # else:
        #    # person just refers to the existing one
            
    def scrape_em_all(self):
        self.populate_recipe_list()
        count = 0
        for recipe in self.recipe_list:
            self.export_recipe_to_app(recipe)
            count = count + 1
            print(count)
            time.sleep(5)

        print("{} Recipes imported".format(count))


# imp = BudgetByteScraper()

# imp.scrape_em_all()