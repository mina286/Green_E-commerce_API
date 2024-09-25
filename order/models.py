from django.db import models
from utils.generation_code import generate_code
from django.utils import timezone
from products.models import Product
from django.contrib.auth.models import User
# Create your models here.
STATUS_CHOICES_CART =(
    ('inprogress','inprogress'),
    ('completed','completed'),


)
class CartOrder(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='cartorder_user')
    code = models.CharField(max_length = 20,default = generate_code)
    cart_order_state = models.CharField(max_length=100,choices=STATUS_CHOICES_CART)
  
    def __str__(self):
        return f"{self.code} {self.user}"
    class Meta:
        db_table = 'CartOrder'
        verbose_name = 'cartorder'
        verbose_name_plural = 'cartorders'

class CartOrderDetail(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,related_name='cartorderdetail_product')
    cart_order = models.ForeignKey(CartOrder,on_delete=models.CASCADE,related_name='cartorderdetail_cartorder')
    price = models.FloatField()
    quantity = models.FloatField()
    total = models.FloatField(default=0)
    
    def __str__(self):
        return f"{self.product} {self.cart_order} {self.quantity}"
    class Meta:
        db_table = 'CartOrderDetail'
        verbose_name = 'cartorderdetail'
        verbose_name_plural = 'cartorderdetails'
    


#######################################
STATUS_CHOICES_ORDER =(
    ('recieved','recieved'),
    ('processed','processed'),
    ('shipped','shipped'),
    ('delivered','delivered'),

)
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='order_user')
    code = models.CharField(max_length = 20,default = generate_code)
    order_state = models.CharField(max_length=100,choices=STATUS_CHOICES_ORDER)
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(null=True,blank=True)
    delivery_fee = models.FloatField()

    def __str__(self):
        return f"{self.code} "
    class Meta:
        db_table = 'Order'
        verbose_name = 'order'
        verbose_name_plural = 'orders'

class OrderDetail(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,related_name='orderdetail_product')
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='orderdetail_order')
    price = models.FloatField()
    quantity = models.FloatField()
    def __str__(self):
        return f"{self.product} {self.order} {self.quantity}"
    class Meta:
        db_table = 'OrderDetail'
        verbose_name = 'orderdetail'
        verbose_name_plural = 'orderdetails'
    

class Coupon(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='coupon_user')
    code_coupon = models.CharField(max_length=100,default=generate_code)
    start_date = models.DateField(null= True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    is_valid = models.BooleanField(default=True)
    coupon_value = models.FloatField(default=0)
    def __str__(self):
        return f"id ={self.id} c = {self.code_coupon} us = {self.user} sd = {self.start_date} ed = {self.end_date} val = {self.coupon_value}"
    class Meta:
        db_table = 'Coupon'
        verbose_name = 'coupon'
        verbose_name_plural = 'coupons'
    
