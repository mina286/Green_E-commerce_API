from django.shortcuts import render
from django.contrib.auth.models import User
from .models import CartOrder,CartOrderDetail,Order,OrderDetail,Coupon
from products.models import Product
from .serializer import CartOrderDetailSerializer,CartOrderSerializer,CouponSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import generics ,mixins
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.

# 1.1  GET  cart order  
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart_order(request):
    try: 
        cart_order = CartOrder.objects.get(user = request.user,cart_order_state = 'inprogress')
        serializer = CartOrderSerializer(cart_order)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as ex :
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)
       

    
# 1.2  POST cart order detail 
@api_view(['POST'])
def create_cart_order_detail(request):
    try:        
            data = request.data
            cartorder = CartOrder.objects.get(id = data['cart_order'])
            # 1 check cartorder is inprogress
            if cartorder.cart_order_state == 'inprogress' :
                # 2 check product not exist already in cart_order_detail
                product = Product.objects.get(id = request.data['product'])
                if CartOrderDetail.objects.filter(product = product).exists():
                    # this case will update to quntity not create 
                    cartorderdetail = CartOrderDetail.objects.get(product = product )
                    serializer = CartOrderDetailSerializer(data=data,instance=cartorderdetail,partial =True)
                    if serializer.is_valid(): 
                        price = serializer.validated_data.get('price')
                        quantity = serializer.validated_data.get('quantity')
                        total = price * quantity
                        serializer.save(total = total)
                        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
                    else:
                        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                # else 2 check product not exist already in cart_order_detail
                else :
                    serializer = CartOrderDetailSerializer(data=data)
                    if serializer.is_valid(): 
                        price = serializer.validated_data.get('price')
                        quantity = serializer.validated_data.get('quantity')
                        total = price * quantity
                        serializer.save(total = total)
                        return Response(serializer.data,status=status.HTTP_201_CREATED)
                    else:
                        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                    
           # else 1 check cartorder is inprogress
            else:
                    return Response({'error':'this cart order status is completed'},status=status.HTTP_400_BAD_REQUEST)
    except Exception as ex :
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)

# 1.3  delete cart order detail 
@api_view(['DELETE'])
def delete_cart_order_detail(request,pk):
    try:        
        cartorderdetail = CartOrderDetail.objects.get(id = pk)
        cartorderdetail.delete()
        return Response({'message':'cartorderdetail is deleted'},status=status.HTTP_204_NO_CONTENT)

    except CartOrderDetail.DoesNotExist :
        return Response({'error':'product not found  '},status=status.HTTP_404_NOT_FOUND)
    except Exception as ex :
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)


# 1.4  POST create_coupon
@api_view(['POST'])
def create_coupon(request):
    try:        
        data = request.data
        serilaizer  =  CouponSerializer(data=data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serilaizer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as ex :
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)

