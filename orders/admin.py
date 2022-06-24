from django.contrib import admin
from .models import Status, Order, ProductInOrder

# class ProductInOrder(admin.TabularInline):
# 	models = ProductInOrder
# 	extra = 0

admin.site.register(Status)

# class Order(Order):
# 	list_display = [field.name for field in Order._meta.fields]
# 	inlines = [ProductInOrder]


# 	class Meta:
# 		model = Order


admin.site.register(Order)
admin.site.register(ProductInOrder)
