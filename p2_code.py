
import requests
from bs4 import BeautifulSoup

from functools import reduce
from operator import concat


import re

def is_url_valid(page_url):
    if type(page_url) is str:
        if re.match(r"https?:\/\/www.allrecipes.com\/recipe\/\d+\/(.*?)\/", page_url)
            return True
    return False


class RecipeManager():

    def __init__(self, page_url):
        # We assume page_url is valid at this point:

        page = requests.get(page_url)
        soup = BeautifulSoup(page.content, 'html.parser')

        ingred_tags = soup.find_all(class_="recipe-ingred_txt")
        ingreds = [ingred_tag.get_text() for ingred_tag in ingred_tags]
        ingreds = [ingred for ingred in ingreds if ingred != "" and ingred != 'Add all ingredients to list']
        if not ingreds:
            # LIKELY DID NOT WORK, GONNA TRY NEW METHOD
            ingred_tags = soup.find_all(class_="ingredients-item-name")
            ingreds = [ingred_tag.get_text() for ingred_tag in ingred_tags]
            ingreds = [ingred.strip() for ingred in ingreds if ingred != "" and ingred != 'Add all ingredients to list']

        prep_tags = soup.find_all(class_="prepTime__item")
        time_tags = [prep_tag.find_all("time")[0] for prep_tag in prep_tags if prep_tag.find_all("time")]
        time_dict = {time_tag['itemprop']: time_tag['datetime'] for time_tag in time_tags}
        if not time_dict:
            # LIKELY DID NOT WORK, GONNA TRY NEW METHOD
            prep_tags = soup.find_all(class_="recipe-meta-item")
            prep_dict = {tag.find(class_="recipe-meta-item-header").get_text().strip()[:-1] : tag.find(class_="recipe-meta-item-body").get_text().strip() for tag in prep_tags}
            time_dict = {key + "Time": time for key, time in prep_dict.items() if key in ["prep", "cook", "total"]}

        steps_tags = soup.find_all(class_="recipe-directions__list--item")
        steps = [steps_tag.get_text().strip() for steps_tag in steps_tags]
        if not steps:
            # LIKELY DID NOT WORK, GONNA TRY NEW METHOD
            steps_tags = soup.find_all(class_="instructions-section-item")
            steps = [steps_tag.find(class_="section-body").get_text().strip() for steps_tag in steps_tags]
        steps = reduce(concat, [step.split(". ") for step in steps if step != ""])        

        self.title = soup.find_all("title")[0].get_text()
        self.ingreds = ingreds
        self.steps = steps
        self.time_dict = time_dict

    def get_title(self):

        return self.title

    def get_cook_times(self):


        return "it takes time to cook"


    def get_ingreds(self):

        return self.ingreds


    def get_step(self, step_no):
        # NOTE: we assume step_no is from a 0-index system
        # Callers to this function must use a 0-index step_no

        return self.steps[step_no]