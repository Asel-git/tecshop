from django.shortcuts import render
from .models import Product



def products(request):
	product_objects = Product.objects.all()
	return render(request, 'products/products.html', {'products': product_objects})



