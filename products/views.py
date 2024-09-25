from django.shortcuts import render
from .serializer import ProductSerializer,CategorySerializer,BrandSerializer,ProductImagesSerializer,ReviewSerializer
from .models import Product,Category,Brand,Review,ProductImages
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAdminUser,IsAuthenticated,BasePermission
from rest_framework import generics,mixins
# Create your views here.

# 1.1 GET Products fbv
@api_view(['GET'])
def products_list(request):
    try:
        products = Product.objects.all()
        serializer =ProductSerializer(products,many =True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)
# 1.2 POST Product fbv
@api_view(['POST'])
def product_create(request):
    try:
        data = request.data
        serializer =ProductSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)
            
# 1.3 GET Product fbv
@api_view(['GET'])
def product_detail(request,slug):
    try:
        product = Product.objects.get(slug = slug)
        serializer =ProductSerializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    except Product.DoesNotExist :
        return Response({'error':'product not found'},status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)
# 1.4 PUT Product fbv
@api_view(['PUT'])
def product_update(request,slug):
    try:
        data = request.data
        product = Product.objects.get(slug = slug)
        serializer =ProductSerializer(data = data,instance = product,partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Product.DoesNotExist :
        return Response({'error':'product not found'},status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)

# 1.5 DELETE Product fbv
@api_view(['DELETE'])
def product_delete(request,slug):
    try:
        product = Product.objects.get(slug = slug)
        product.delete()
        return Response({'message':'product is deleted'},status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist :
        return Response({'error':'product not found'},status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)
    
# 2.1 GET POST Category Generics
class Generics_Category(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
# 2.2 GET PUT DELETE Category Generics
class Generics_Category_Slug(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

# 3.1 GET POST Mixins brand
class Mixins_Brand(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
# 3.2 GET PUT DELETE Mixins brand 
class Mixins_Brand_Slug(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'slug'
    def get(self,request,slug):
        return self.retrieve(request)
    def put(self,request,slug):
        return self.update(request)
    def delete(self,request,slug):
        return self.destroy(request)
    
# 4.1 GET POST ProductImages Generics
class Generics_ProductImages(generics.ListCreateAPIView):
    queryset =ProductImages.objects.all()
    serializer_class = ProductImagesSerializer

# 4.2 GET PUT DELETE ProductImages Generics
class Generics_ProductImages_PK(generics.RetrieveUpdateDestroyAPIView):
    queryset =ProductImages.objects.all()
    serializer_class = ProductImagesSerializer

# 5.1 GET POST Review Generics
class Generics_Review(generics.ListCreateAPIView):
    queryset =Review.objects.all()
    serializer_class = ReviewSerializer

# 5.2 GET PUT DELETE Review Generics
class Generics_Review_PK(generics.RetrieveUpdateDestroyAPIView):
    queryset =Review.objects.all()
    serializer_class = ReviewSerializer