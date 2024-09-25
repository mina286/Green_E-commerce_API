from django.contrib import admin
from .models import CartOrder,CartOrderDetail,Order,OrderDetail,Coupon
# Register your models here.
# 
class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['id','user','code','cart_order_state']
    list_display_links = ['id','user','code','cart_order_state']
admin.site.register(CartOrder,CartOrderAdmin)
# 
class CartOrderDetailAdmin(admin.ModelAdmin):
    list_display = ['id','product','cart_order','price','quantity','total']
    list_display_links = ['id','product','cart_order','price','quantity','total']
admin.site.register(CartOrderDetail,CartOrderDetailAdmin)
# 
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','user','code','order_state','delivery_time']
    list_display_links = ['id','user','code','order_state','delivery_time']
admin.site.register(Order,OrderAdmin)
# 
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['id','product','order','price','quantity']
    list_display_links = ['id','product','order','price','quantity']
admin.site.register(OrderDetail,OrderDetailAdmin)
# 
class CouponAdmin(admin.ModelAdmin):
    list_display = ['id','user','code_coupon','coupon_value','start_date','end_date','is_valid']
    list_display_links = ['id','user','code_coupon','coupon_value','start_date','end_date','is_valid']
admin.site.register(Coupon,CouponAdmin)