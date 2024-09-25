from django.contrib.auth.models import User
from .models import Profile,PhoneNumber,Address,ActivationCode
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core import validators
from rest_framework import validators
class UserSerializer(serializers.ModelSerializer):
   
    
    def create(self,data):
        password = data.pop('password')
        user = User(**data)
        user.set_password(password)
        user.save()
        return user

    def update(self,instance,data):
        password = data.pop('password')
        instance.set_password(password)
        return super().update(instance,data)
    
   
    
    class Meta:
        model = User
        fields = '__all__'


# 2
class ChangPasswordSerializer(serializers.Serializer):
    
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True,validators=[validate_password])
 

# 3
class AdressSerializer(serializers.ModelSerializer):
    class Meta :
        model = Address
        fields = '__all__'
 

# 4
class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta :
        model = PhoneNumber
        fields = '__all__'
# 5
class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(write_only =True,queryset = User.objects.all())
    user_detail = serializers.SerializerMethodField(read_only =True)
    def get_user_detail(self,obj):
       user = obj.user
       serializer = UserSerializer(user)
       return serializer.data
    
    phone_numbers = serializers.SerializerMethodField(read_only =True)
    def get_phone_numbers(self,obj):
       phone_numbers = obj.user.phonenumber_user.all()
       serializer = PhoneNumberSerializer(phone_numbers,many =True)
       return serializer.data
 
    address = serializers.SerializerMethodField(read_only =True)
    def get_address(self,obj):
       address = obj.user.address_user.all()
       serializer = AdressSerializer(address,many =True)
       return serializer.data
   
    class Meta :
        model = Profile
        fields = '__all__'
 
