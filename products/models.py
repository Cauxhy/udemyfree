# products/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.name

# products/models.py
class Product(models.Model):
    title = models.CharField(max_length=255)  # Le titre du cours
    course_url = models.URLField(max_length=200)  # L'URL du cours
    image_url = models.URLField(max_length=200)  # L'URL de l'image du cours
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # La catégorie du cours
    languages = models.TextField(blank=True)  # Langues disponibles pour le cours
    author = models.CharField(max_length=255, blank=True)  # Auteur du cours
    rating = models.CharField(max_length=50, blank=True)  # Note du cours
    enroll_count = models.CharField(max_length=50, blank=True)  # Nombre d'inscriptions
    old_price = models.CharField(max_length=50, blank=True)  # Ancien prix
    new_price = models.CharField(max_length=50, blank=True)  # Nouveau prix
    free_code_url = models.URLField(max_length=200, blank=True)  # URL du code gratuit

    def __str__(self):
        return self.title
