from django.contrib import admin

# Register your models here.
from product.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'price',
                    'created_at', 'image', 'thumbnail')
    prepopulated_fields = {'slug': ('name',)}
