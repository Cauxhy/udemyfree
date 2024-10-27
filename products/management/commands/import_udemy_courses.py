# products/management/commands/import_udemy_courses.py
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from products.models import Product, Category

class Command(BaseCommand):
    Product.objects.all().delete()
  
    help = 'Scrape Udemy courses and save them to the database'

    def handle(self, *args, **kwargs):
        base_url = "https://www.udemyfreebies.com/free-udemy-courses"
        page_number = 1
        
        while True:
            url = f"{base_url}/{page_number}" if page_number > 1 else base_url
            response = requests.get(url)
            
            if response.status_code != 200:
                self.stdout.write("No more pages to scrape or an error occurred.")
                break
            
            soup = BeautifulSoup(response.content, "html.parser")
            course_cards = soup.find_all("div", class_="col-md-4 col-sm-6")
            if not course_cards:
                self.stdout.write("No more course cards found, stopping scraping.")
                break
            
            for card in course_cards:
                title = card.find("h4").get_text(strip=True)
                course_url = card.find("a", class_="theme-img")["href"]
                img_url = card.find("img")["src"]

                category_name = card.find("div", class_="coupon-specility").get_text(strip=True)
                category, created = Category.objects.get_or_create(name=category_name)

                language_elements = card.find_all("p")
                languages = [lang.get_text(strip=True) for lang in language_elements if any(lang_text in lang.get_text() for lang_text in ["English", "French", "Spanish", "Business"])]
                author = card.find("p", class_="fa-user")
                author = author.get_text(strip=True) if author else "N/A"
                rating = card.find("p", class_="fa-star")
                rating = rating.get_text(strip=True) if rating else "N/A"
                enroll_count = card.find("p", class_="fa-users")
                enroll_count = enroll_count.get_text(strip=True) if enroll_count else "N/A"
                price_info = card.find("p", class_="fa-money")
                old_price, new_price = "N/A", "Free"

                if price_info:
                    price_text = price_info.get_text(strip=True)
                    if "->" in price_text:
                        old_price, new_price = map(str.strip, price_text.split("->"))
                    else:
                        old_price = price_text
                
                # Suivez le lien du cours pour obtenir le code promo
                promo_code = self.get_promo_code(course_url)

                # Enregistrez dans la base de données uniquement si le produit n'existe pas déjà
                if not Product.objects.filter(course_url=course_url).exists():
                    Product.objects.create(
                        title=title,
                        course_url=course_url,
                        image_url=img_url,
                        category=category,
                        languages=", ".join(languages),
                        author=author,
                        rating=rating,
                        enroll_count=enroll_count,
                        old_price=old_price,
                        new_price=new_price,
                        free_code_url=promo_code,  # Stockez le code promo
                    )
            
            self.stdout.write(f"Scraped page {page_number}")
            page_number += 1

    def get_promo_code(self, course_url):
        """Scrape the promo code from the course page."""
        response = requests.get(course_url)
        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.content, "html.parser")
        
        # Rechercher l'élément qui contient le code promo
        promo_element = soup.find("a", class_="button-icon")  # Adaptez le sélecteur à la structure réelle de la page
        return promo_element["href"] if promo_element else None
