from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils.text import slugify
FLAG_TYPE = (
    ('new','new'),
    ('feature','feature'),

)
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length= 100)
    sku = models.IntegerField()
    brand =  models.ForeignKey("Brand",on_delete= models.SET_NULL,null=True,related_name='product_brand')
    price = models.FloatField()
    description = models.TextField()
    flag =models.CharField(max_length=20,choices=FLAG_TYPE)
    category =  models.ForeignKey("Category",on_delete= models.SET_NULL,null=True,related_name='product_category')
    image = models.ImageField(upload_to='product/',default='/default_image/def.jpg')
    slug = models.SlugField(null=True,blank=True)
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0,max_digits=10,decimal_places=2)
    is_out_of_stock = models.BooleanField(default=False)
    number_of_stock = models.FloatField(default=0,validators=[MinValueValidator(0)])

    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)
       super(Product, self).save(*args, **kwargs) 
    
    def __str__(self):
        return f"{self.name} {self.price}"
    class Meta:
        db_table = 'Product'
        verbose_name = 'product'
        verbose_name_plural = 'products'
        constraints = [
            models.CheckConstraint(check=models.Q(number_of_stock__gte= 0),name='number_of_stock__gte0')
        ]

class Brand(models.Model):
    name = models.CharField(max_length= 100)
    slug = models.SlugField(null=True,blank=True)
    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)
       super(Brand, self).save(*args, **kwargs) # Call the real save() method
    def __str__(self):
        return f"{self.name} "
    class Meta:
        db_table = 'Brand'
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class Category(models.Model):
    name = models.CharField(max_length= 100)
    image = models.ImageField(upload_to='category_images/',default='/default_image/def.jpg')
    slug = models.SlugField(null=True,blank=True)
    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)
       super(Category, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return f"{self.name} "
    class Meta:
        db_table = 'Category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class Review(models.Model):
    product =  models.ForeignKey(Product,on_delete= models.CASCADE,related_name='review_product')
    user =  models.ForeignKey(User,on_delete= models.SET_NULL,null=True,related_name='review_user')
    review = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    rate = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    def __str__(self):
        return f"{self.review} {self.user}"
    class Meta:
        db_table = 'Review'
        verbose_name = 'review'
        verbose_name_plural = 'reviews'
        constraints =[
            models.CheckConstraint(check=models.Q(rate__gte=0)&models.Q(rate__lte=5),name="rate0-5")
        ]

class ProductImages(models.Model):
    product =  models.ForeignKey(Product,on_delete= models.CASCADE,related_name='productimages_product')
    image = models.ImageField(upload_to='product_images/')
    def __str__(self):
        return f"{self.product} "
    class Meta:
        db_table = 'ProductImages'
        verbose_name = 'productimage'
        verbose_name_plural = 'productimages'
