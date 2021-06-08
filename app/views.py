from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView



class Home(ListView):
 model = Product
 template_name = 'index.html'

class ProductDetail(DetailView):
 model = Product
 template_name = 'productdetail.html'
# def home(request):
#  pro = Product.objects.all
#  return render(request, 'index.html', {'pro':pro})

def about(request):
 return render(request, 'about.html')
 

def contact(request):
 return render(request, 'contact.html')
