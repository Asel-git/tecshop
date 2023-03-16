from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Product(models.Model):
	
	name = models.CharField(max_length=150, null=True, blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	category = models.ForeignKey(Category, on_delete = models.CASCADE, default='', null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	available = models.BooleanField(default=True)
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
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, default=None)
	photo = models.ImageField(
		upload_to='products_images',
		null=True, blank=True
	)
	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Картина'
		verbose_name_plural = "Картины"
		
