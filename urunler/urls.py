from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.urunler, name='urunler'),
    path('<slug:category_slug>/<int:urun_id>', views.urun_detay, name='urun_detay'),
    path('categories/<slug:category_slug>', views.urunler, name='uruns_by_kategory'),
    path('tags/<slug:tag_slug>', views.urunler, name='tags_by_kategory'),
    path('search/', views.search, name='search'),
   
]