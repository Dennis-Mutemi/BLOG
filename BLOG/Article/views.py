from django.shortcuts import render,redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms
# Create your views here.
def indexx(request):
    articles =Article.objects.all().order_by('date')
    return render(request,'articles/index.html',{'article': articles})
def article_details(request,me):
    artivle1=Article.objects.get(slug = me)
    return render(request,'articles/detailed.html',{'article_val': artivle1})

@login_required(login_url="/accounts/login")
def create(request):
    if request.method=='POST':
         formm=forms.CreateArticle(request.POST,request.FILES)
         if formm.is_valid():
            instance=formm.save(commit=False)
            instance.uthor=request.user
            instance.save()
            return redirect('accounts:login')
            
    else:
       formm=forms.CreateArticle()
    return render(request,'articles/create.html',{"form":formm})