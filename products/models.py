from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=70, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	views_count = models.IntegerField(default=0)
	

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = "Товары"
		ordering = ['name']


# class ProductImage(models.Model):
# 	product = models.ForeignKey(Product, null=True, blank=True, default=None)
# 	image = models.ImageField(upload_to='products_images/')
# 	is_active = models.BooleanField(default=True)
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)
	
	

# 	def __str__(self):
# 		return self.name

# 	class Meta:
# 		verbose_name = 'Картина'
# 		verbose_name_plural = "Картины"
# 		ordering = ['name']

