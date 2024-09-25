from .models import CartOrder,CartOrderDetail,Order,OrderDetail,Coupon
from rest_framework import serializers

# 1
class CartOrderDetailSerializer(serializers.ModelSerializer):
   
    class Meta :
        model = CartOrderDetail
        fields = "__all__"
# 2
class CouponSerializer(serializers.ModelSerializer):
    class Meta :
        model = Coupon
        fields = "__all__"

# 3
class CartOrderSerializer(serializers.ModelSerializer):
    #
    total_item = serializers.SerializerMethodField(read_only =True)
    def get_total_item(self,obj):
        total_item = obj.cartorderdetail_cartorder.all().count()
        return total_item
    #
    total_price = serializers.SerializerMethodField(read_only =True)
    def get_total_price(self,obj):     
        try:
            cart_order_detail = obj.cartorderdetail_cartorder.all()
            total_list = []
            for product in cart_order_detail :
                total_list.append(product.total)
            total_price = sum(total_list)
            return total_price
        except :
            return "error happend"
    """ 
    def get_total_price(self,obj):     
        try:
            cart_order_detail = obj.cartorderdetail_cartorder.all()
            coupon = Coupon.objects.get(user = obj.user , is_valid = True) 
            print ('coupon====',coupon)   
            total_list = []
            for product in cart_order_detail :
                total_list.append(product.total)
            total_price = sum(total_list)
            total_with_coupon = float(total_price) - float(coupon.coupon_value)
            return total_with_coupon
        except Coupon.DoesNotExist:
            print(' no coupon ')
            total_list = []
            for product in cart_order_detail :
                total_list.append(product.total)
            total_price = sum(total_list)
            return total_price
        except :
            coupon = Coupon.objects.filter(user = obj.user , is_valid = True).order_by('start_date').first()
            print ('coupon====',coupon)   
            total_list = []
            for product in cart_order_detail :
                total_list.append(product.total)
            total_price = sum(total_list)
            total_with_coupon = float(total_price) - float(coupon.coupon_value)
            return total_with_coupon
       
"""         

    
    #
    cart_oder_detail = serializers.SerializerMethodField(read_only =True)
    def get_cart_oder_detail(self,obj):
        cart_oder_detail = obj.cartorderdetail_cartorder.all()
        serializer = CartOrderDetailSerializer(cart_oder_detail,many=True)
        return serializer.data
    
    class Meta :
        model = CartOrder
        fields = "__all__"