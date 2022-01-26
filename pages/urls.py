from django import views
from django.urls import path
from . import views
from pages.views import AboutView
from pages.views import IndexView
from pages import views as contact_views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/',  AboutView.as_view(), name='about'),
     path('contact/', contact_views.contact_view, name='contact'),
]
