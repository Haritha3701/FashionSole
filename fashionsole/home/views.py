from django.shortcuts import render
from django.http.response import HttpResponse
from products.models import products,category

# Create your views here.
def homepage(request):
    types=category.objects.all()
    
    return render(request,"home.html",{"types":types})