from django.urls import path, include, re_path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.game_selection, name='games'),
    path('guess_number/', views.guess_number, name='guess_number'),
    path('guess_word/', views.guess_word, name='guess_word'),
]