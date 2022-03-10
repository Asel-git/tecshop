from django.shortcuts import render

from .models import Order



def orders(request):
	order_objects = Order.objects.all()
	return render(request, 'orders.html', {'orders': order_objects})

