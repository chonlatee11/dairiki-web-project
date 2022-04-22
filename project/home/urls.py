from cProfile import Profile
from turtle import home
from django.urls import path
from .views import *
urlpatterns = [
    path('',Home),
    path('profile/',Profile, name= 'Profile'),
    path('product/',Product, name= 'Product'),
    path('equipment/',Equipment, name= 'Equipment'),
    path('parent/',Parent, name= 'Parent'),
    path('location/',Location, name= 'Location'),
]