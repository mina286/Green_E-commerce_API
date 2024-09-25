from django.urls import path
from . import views
app_name = "order"
urlpatterns = [
    # 1.1  GET cart order  
    path('cart_order/',views.cart_order,name='cart_order'),
    # 1.2  POST cart order detail 
    path('create_cart_order_detail/',views.create_cart_order_detail,name='create_cart_order_detail'),
    # 1.3  delete cart order detail 
    path('delete_cart_order_detail/<int:pk>/',views.delete_cart_order_detail,name='delete_cart_order_detail'),
    # 1.4  POST create_coupon
    path('create_coupon/',views.create_coupon,name='create_coupon'),


]
