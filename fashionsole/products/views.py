from django.shortcuts import render,redirect
from . models import products,category


# Create your views here.
def product(request):
    categoryid=request.GET["category"]
    data=products.objects.filter(type_id=categoryid)
    return render(request,"products.html",{"cat":data})
        
    
   
def details(request):
    id=request.GET["id"]
    desc=products.objects.get(id=id)
    return render(request,"details.html",{"i":desc})