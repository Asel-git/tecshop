from django.core.management.base import BaseCommand, CommandError
from products.models import Category, Product

lst = ['TV', 'Car', 'Telephone', 'Laptop']
lst2 = ['TV product', 'Car product', 'Telephone product', 'Laptop product']

class Command(BaseCommand):
	def handle(self, *args, *options):
		print('Loading category!')
		Category.objects.all().delete()
		Product.objects.all().delete()
		for i in lst:
			c = Category()
			c.name = i
			c.save()
			for i in lst2:
				p = Product()
				p.name = i
				p.category = c
				p.save()