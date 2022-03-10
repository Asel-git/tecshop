from django.db import models
from products.models import Product

class Status(models.Model):
	name = models.CharField(max_length=24, null=True, blank=True)
	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Статус заказа'
		verbose_name_plural = "Статусы заказа"


class Order(models.Model):
	customer_name = models.CharField(max_length=70, null=True, blank=True)
	customer_email = models.EmailField(null=True, blank=True, default=None)
	customer_phone = models.CharField(max_length=48, null=True, blank=True, default=None)
	comments = models.TextField(null=True, blank=True, default=None)
	status = models.ForeignKey(Status,  on_delete=models.CASCADE, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	

	def __str__(self):
		return (self.id, self.status.name)

	class Meta:
		verbose_name = 'Заказ'
		verbose_name_plural = "Заказы"
	


# class ProductInOrder(models.Model):
# 	order = models. ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
# 	product = models. ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, default=None)
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now_add=True)
	

# 	def __str__(self):
# 		return self.product.name

# 	class Meta:
# 		verbose_name = 'Товар'
# 		verbose_name_plural = "Товары"
# 		ordering = ['name']


