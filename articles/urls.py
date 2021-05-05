from django.urls import path, include, re_path #path - jest potrzebne do utworzenia sciezki przekierowujacej nizej
from . import views # z tego samego folderu importujemy views. Bo właśnie tam bedziemy odsyłać
urlpatterns = [
    path('show_all/', views.articles, name='articles'), #path(ścieżka)(funkcja w danym pliku, nazywamy ja)
    path('<int:article_id>/', views.article, name='article') #path(ścieżka)(funkcja w danym pliku, nazywamy ja)
    ]

# po wpisaniu np. <nazwa strony>/show_all/, plik urls.py musi wyświetlic podana zawartosc z pliku viewz.py..