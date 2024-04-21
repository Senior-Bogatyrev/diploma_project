from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('draft/', views.draft, name='draft'),
    path('<int:post_id>/delete/', views.draft_delete, name='draft_delete'),
    path('<int:post_id>/edit/', views.draft_edit, name='draft_edit'),
    path('<int:post_id>/publish/', views.draft_to_publish, name='draft_to_publish'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
]