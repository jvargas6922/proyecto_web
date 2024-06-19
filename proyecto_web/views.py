from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse('Hola mundo!!!!')
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request,'contact.html')

def news(request):
    return render(request,'news.html')