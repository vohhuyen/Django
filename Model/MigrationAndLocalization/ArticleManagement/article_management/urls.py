from django.urls import path
from .views import article_list, article_detail, article_create, article_update, article_delete, article_list_view, search_articles_view

urlpatterns = [
    path('', article_list_view, name='article_list'),
    path('article/<int:pk>/', article_detail, name='article_detail'),
    path('article/new/', article_create, name='article_create'),
    path('article/search/', search_articles_view, name='article_search'),
    path('article/<int:pk>/edit/', article_update, name='article_update'),
    path('article/<int:pk>/delete/', article_delete, name='article_delete'),
]
