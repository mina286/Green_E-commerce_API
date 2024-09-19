from django.contrib import admin
from .models import Product,Category,Brand,ProductImages,Review
# Register your models here

# 1
class ProductIamgesInlines(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','brand','category','price','image']
    list_display_links = ['name','brand','category','price','image']
   # inlines = [ProductIamgesInlines]
admin.site.register(Product,ProductAdmin)
# 2
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
admin.site.register(Category,CategoryAdmin)
# 3
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
admin.site.register(Brand,BrandAdmin)
# 4
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ['product','image']
    list_display_links = ['product','image']
admin.site.register(ProductImages,ProductImagesAdmin)
# 5
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product','user','review','rate']
    list_display_links = ['product','user','review','rate']
admin.site.register(Review,ReviewAdmin)