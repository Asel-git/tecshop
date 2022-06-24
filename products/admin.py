from django.contrib import admin
from .models import Product, ProductImage

class ProductImageInline(admin.TabularInline):
	models = ProductImage
	extra = 0

admin.site.register(Product)
admin.site.register(ProductImage)
