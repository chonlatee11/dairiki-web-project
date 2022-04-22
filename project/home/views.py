from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
    return render(request,'home/home.html')
def Profile(request):
    return render(request,'home/profile.html')
def Product(request):
    return render(request,'home/product.html')
def Equipment(request):
    return render(request,'home/equipment.html')
def Parent(request):
    return render(request,'home/parent.html')
def Location(request):
    return render(request,'home/location.html')
