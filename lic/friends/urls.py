from django.urls import path
from . import views

app_name = 'friends'

urlpatterns = [
    path('', views.friends_list, name='friends_list'),
    path('search', views.search_users, name='search_users'),
    path('add_friend', views.add_friend, name='add_friend'),
    path('followers', views.followers, name='followers'),
] 