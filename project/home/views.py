import email
from email import message
from hashlib import new
from logging import exception
from multiprocessing import context
from re import sub
import re
from turtle import title
from django.shortcuts import render
from django.http import BadHeaderError, HttpResponse
from .models import *
from django.conf import settings
from django.core.mail import send_mail
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

def Contact(request):
    context = {}
    if request.method == 'POST':
        data = request.POST.copy()
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        detail = data.get('detail')
        #print(subject,email,detail)
        if name == '' and email == '' and subject == '' and detail == '':
            context['status'] = 'alert'
            return render(request,'home/contact.html',context)
        new = ContactMessage()
        new.name = name
        new.email = email
        new.subject = subject
        new.detail = detail
        
        subjectmail = f'Message form {email}'
        message = f'Subject {subject} \n {detail}'
        sender = settings.EMAIL_HOST_USER
        #เมลล์ของบริษัท
        recipents = ['chonlatee1129@gmail.com']
        send_mail(
                subjectmail,message,sender,recipents,fail_silently=False,
        )
        new.save()
        context['status'] = 'success'
    return render(request,'home/contact.html',context)

def Location(request):
    return render(request,'home/location.html')