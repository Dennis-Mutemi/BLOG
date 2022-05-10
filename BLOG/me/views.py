from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return HttpResponse('HOME PAGE')
def about(request):
    return render(request,'home.html')