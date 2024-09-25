from .models import Product,Brand,Category,Review,ProductImages
from rest_framework import serializers

# 1
class ProductSerializer(serializers.ModelSerializer):

    review = serializers.SerializerMethodField(read_only =True)
    def get_review(self,obj):
        reviews = obj.review_product.all()
        serializer = ReviewSerializer(reviews,many =True)
        return serializer.data
    
    number_of_reviews = serializers.SerializerMethodField(read_only =True)
    def get_number_of_reviews(self,obj):
        number = obj.review_product.all().count()
        return number
    
    product_images = serializers.SerializerMethodField(read_only =True)
    def get_product_images(self,obj):
        product_images = obj.productimages_product.all()
        serializer= ProductImagesSerializer(product_images,many =True)
        return serializer.data
    
    
       
        
    class Meta:
        model = Product
        fields  = "__all__"
# 2
class CategorySerializer(serializers.ModelSerializer):
    number_of_products = serializers.SerializerMethodField(read_only =True)
    def get_number_of_products(self,obj):
        number = obj.product_category.all().count()
        return number

    class Meta:
        model = Category
        fields  = "__all__"
# 3
class BrandSerializer(serializers.ModelSerializer):
    number_of_products = serializers.SerializerMethodField(read_only =True)
    def get_number_of_products(self,obj):
        number = obj.product_brand.all().count()
        return number
    
    class Meta:
        model = Brand
        fields  = "__all__"
# 4
class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields  = "__all__"

# 5
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields  = "__all__"