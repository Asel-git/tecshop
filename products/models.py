from django.db import models
# from django.contrib.auth.models import User

# class Category(models.Model):
#     name = models.CharField(max_length=200, null=True, blank=True)
#     slug = models.SlugField(max_length=200, db_index=True, unique=True)
	
	
#     class Meta:
#         ordering = ['name']
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'

#     def __str__(self):
#         return self.name



class Product(models.Model):
	# category = models.ForeignKey(Category, 
	# 							related_name='products', 
	# 							on_delete = models.CASCADE)
	name = models.CharField(max_length=150, null=True, blank=True)
	# slug = models.SlugField(max_length=200, db_index=True, unique=True)
	price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	available = models.BooleanField(default=True)
	# created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	photo = models.ImageField(
		upload_to='products_images',
		null=True, blank=True
	)
	
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'
		ordering = ['name']


class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, default=None)
	image = models.ImageField(upload_to='products_images/')
	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Картина'
		verbose_name_plural = "Картины"
		
