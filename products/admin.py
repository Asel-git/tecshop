from django.contrib import admin
from .models import Product, ProductImage, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category']
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)