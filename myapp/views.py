from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"myapp/home.html")

def profile(request):
    name="Souvik"
    return render(request,"myapp/profile.html",{'name':name})

def sample1(request):
    vegetable = ['potato','tomato','carrot','cabbage','onion']
    return render(request,"myapp/sample1.html",{'vegetable':vegetable})
    
def sample2(request):
    fruits = ['apple','banana','guava','watermelon','mango']
    return render(request,"myapp/sample2.html",{'fruits':fruits})
