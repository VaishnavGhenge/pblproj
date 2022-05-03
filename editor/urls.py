from django import views
from django.urls import path
from .import views

urlpatterns = [
    path('', views.save_data, name='signup'),
    path('retrieve/', views.retrieve_data, name='retrieve')
]