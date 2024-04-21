from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_selection, name='games'),
    path('guess_number/', views.guess_number, name='guess_number'),
    path('guess_word/', views.guess_word, name='guess_word'),
]