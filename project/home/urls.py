from cProfile import Profile
from turtle import home
from django import views
from django.urls import path
from .views import *
urlpatterns = [
    path('',Home),
    path('profile/',Profile, name= 'Profile'),
    path('product/',Product, name= 'Product'),
    path('equipment/',Equipment, name= 'Equipment'),
    path('contact/',Contact, name= 'Contact'),
    path('location/',Location, name= 'Location'),
]