from unicodedata import name
from django import views
from django.urls import path
from .import views

urlpatterns = [
    path('', views.overview, name='overview'),
    path('save/', views.save_data, name='save-data'),
    path('retrieve/', views.retrieve_data, name='retrieve'),
    path('authenticate/', views.authenticate, name='auhtenticate'),
]