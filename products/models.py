from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator,MinValueValidator
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
    tags = ""
    flag =models.CharField(max_length=20,choices=FLAG_TYPE)
    category =  models.ForeignKey("Category",on_delete= models.SET_NULL,null=True,related_name='product_category')
    image = models.ImageField(upload_to='product/')

    def __str__(self):
        return f"{self.name} {self.price}"
    class Meta:
        db_table = 'Product'
        verbose_name = 'product'
        verbose_name_plural = 'products'

class Brand(models.Model):
    name = models.CharField(max_length= 100)
    def __str__(self):
        return f"{self.name} "
    class Meta:
        db_table = 'Brand'
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class Category(models.Model):
    name = models.CharField(max_length= 100)
    image = models.ImageField(upload_to='category_images/')

    def __str__(self):
        return f"{self.name} "
    class Meta:
        db_table = 'Category'
        verbose_name = 'category'
        verbose_name_plural = 'categorys'

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
