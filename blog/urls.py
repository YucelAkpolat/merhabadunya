from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:category_slug>/<int:post_id>', views.blog_detay, name='blog_detay'),
    path('categories/<slug:category_slug>', views.blog_kategory, name='blog_by_kategory'),
    path('tags/<slug:tag_slug>', views.tag_kategory, name='tags_by_blog'),
    path('search/', views.search, name='search'),
]
