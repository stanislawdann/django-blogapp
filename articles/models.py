#-*- coding: utf-8 -*-
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Tytuł")
    content = models.TextField(verbose_name="zawartość")
    published = models.DateTimeField(verbose_name="Data publikacji")
    image = models.FileField(upload_to="images", verbose_name="Obrazek")

    def __str__(self):
        return self.title
        #zamiast generatora, zwraca verbose name

# Stworzyłem klase "Article", ktora posiada 4 pola modelu:
# title - atrybut klasy odpowiadający za tytuł. Instacja klasy field "CharField", umożliwia mu podanie 150 znakow.
# content - atrybut klasy odpowiadający za opis. Instacja klasy field "TextField", umożliwia mu podanie nielimitowanej ilosci znakow.
# published - atrybut klasy odpowiadający za opis. Instancja klasy DataTimeField, umożliwia mu przechowywanie daty i czasu.
# image - atrybut klasy odpowiadający za upload plików. Instancja klasy "FileField", umożliwia mu uploadowac pliki do folderu images.

# każdy atrybu reprezentuje jedno pole w tabeli articles_Article
# każdy model trzeba zdefiniowac w settings.py w zmiennej INSTALLED_APPS


#upload_to - sprawdza w settings.py gdzie(media_url i media_root) ma zuploadować
#plik, chyba że nie ma takiego folderu to go stworzy. Wtedy wszystkie zdjęcia będa przechowywane w "chmurze"