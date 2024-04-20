from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('settings/', views.settings, name='settings'),
    path('message/', views.message, name='message'),
    path('friends/', views.friends, name='friends'),
    path('news/', include('news.urls', namespace='news')),
    path('games/', include('games.urls')),
]