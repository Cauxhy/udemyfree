# products/management/commands/import_udemy_categories.py
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from products.models import Category

class Command(BaseCommand):
    help = 'Scrape Udemy categories and save them to the database'

    def handle(self, *args, **kwargs):
        url = "https://www.udemyfreebies.com/course-categories"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        categories_list = soup.find("ul", class_="category-list").find_all("li")

        for category in categories_list:
            category_name = category.get_text(strip=True).split('(')[0].strip()
            category_url = category.find("a")["href"]

            # Create or update category in the database
            Category.objects.get_or_create(name=category_name, url=category_url)
        
        self.stdout.write("Categories scraped and saved to the database.")
