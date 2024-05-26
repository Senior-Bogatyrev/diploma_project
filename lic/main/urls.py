from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('settings/', views.settings, name='settings'),
    path('user/<int:user_id>', views.user, name='user'),
    path('friends/', include('friends.urls', namespace='friends')),
    path('news/', include('news.urls', namespace='news')),
    path('games/', include('games.urls')),
    path('message/', include('message.urls')),
]