from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.
def index(request):
       products = Product.objects.all()
       print(products)
       n= len(products)
       nSlides=n//4 *ceil((n/4)-(n//4))
       params={'no_of_slides' : nSlides, 'range' : range(1, nSlides), 'product' : products}
       return render(request,'shop/index.html',params)


def about(request):
    return render(request,"shop/about.html")
def contact(request):
    return HttpResponse("hello ata contact")
def tracker(request):
    return HttpResponse("hello ata tracker")
def search(request):
    return HttpResponse("hello ata search t")
def productionview(request):
    return HttpResponse("hello ata productionview")
def checkout(request):
    return HttpResponse("hello ata chekcout")