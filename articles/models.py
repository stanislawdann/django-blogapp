#-*- coding: utf-8 -*-
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Tytuł")
    content = models.TextField(verbose_name="zawartość")
    published = models.DateTimeField(verbose_name="Data publikacji")

    def __str__(self):
        return self.title