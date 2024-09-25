from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile,PhoneNumber,Address,ActivationCode
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer,ChangPasswordSerializer,AdressSerializer,PhoneNumberSerializer,ProfileSerializer
from django.core.mail import send_mail
from project.settings import EMAIL_HOST_USER
from rest_framework import generics , mixins
# Create your views here.

# 1.1 GET users fbv
@api_view(['GET'])
def users(request):
    try:
        users = User.objects.all()
        serializer =UserSerializer(users,many =True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)

# 1.2 GET user fbv
@api_view(['GET'])
def user_detail(request,pk):
    try:
        user = User.objects.get(id = pk)
        serializer =UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    except User.DoesNotExist:
        return Response({'error':'user not found '},status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)

# 1.3 POST user fbv
@api_view(['POST'])
def signup(request):
    try:
        data = request.data
        serializer =UserSerializer(data = data)
        if serializer.is_valid():
            is_active = serializer.validated_data.get('is_active')
            serializer.save(is_active = False)
            user_data = serializer.data
            email = user_data['email']

            user_id = user_data['id']
            activationcode = ActivationCode.objects.get(user = user_id)
            print('activatiocode==',activationcode)
            send_mail(
                "active code from Green E_commerce",
                f"to activate your account Green E_commerce, please use this code {activationcode.code}",
                EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return redirect(f'/accounts/check_code_activate/{user_id}/')
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)

# 1.4 POST check_code_activate  user fbv
@api_view(['POST'])
def check_code_activate(request,pk):
    try:
        
        # pk = user_id 
        activationcode = ActivationCode.objects.get(user = pk)
        user = User.objects.get(id =pk)
        data = request.data
        if activationcode.code == data['code']:
            activationcode.code_used = True
            activationcode.save()
            user.is_active = True
            user.save()
            return Response({'message':'account is active successful'},status=status.HTTP_200_OK)
        else:
            return Response({'error':'code is not correct'},status=status.HTTP_400_BAD_REQUEST)
        
   
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)
 
# 1.5 PUT user fbv
@api_view(['PUT'])
def user_update(request,pk):
    try:
        data = request.data
        user = User.objects.get(id = pk)
        serializer =UserSerializer(data = data,instance =user,partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({'error':'user not found '},status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)

# 1.6 DELETE user fbv
@api_view(['DELETE'])
def user_delete(request,pk):
    try:
        user = User.objects.get(id = pk)
        user.delete()
        return Response({'message':'user is deleted'},status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response({'error':'user not found '},status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)

# 1.7 change password manual user fbv
@api_view(['POST'])
def change_password(request):
    try:
        # pk = user_id 
        user = User.objects.get(id = 22)
        serializer = ChangPasswordSerializer(data=request.data)
        if serializer.is_valid():
            if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.save()
                return Response({'message':'password is change  successful'},status=status.HTTP_200_OK)
            else:
                return Response({'error':'incorrect in old password '},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as ex:
        return Response({'error':f'error happend1 {ex}'},status=status.HTTP_400_BAD_REQUEST)

# 1.8 reset password manual user fbv
@api_view(['POST'])
def reset_password(request):
   pass
# 2.1 GET Profile fbv
@api_view(['GET'])
def profiles(request):
    try:
        profiles = Profile.objects.all()
        serializer =ProfileSerializer(profiles,many =True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)
# 2.2 POST Profile fbv
@api_view(['POST'])
def profile_create(request):
    try:
        data = request.data
        serializer =ProfileSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)
# 2.3 GET Profile fbv
@api_view(['GET'])
def profile_detail(request,pk):
    try:
        profile = Profile.objects.get(id = pk)
        serializer =ProfileSerializer(profile)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    except User.DoesNotExist:
        return Response({'error':'profile not found '},status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)

# 2.4 PUT Profile fbv
@api_view(['PUT'])
def profile_update(request,pk):
    try:
        data = request.data
        profile = Profile.objects.get(id = pk)
        serializer =ProfileSerializer(data = data,instance =profile,partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Profile.DoesNotExist:
        return Response({'error':'profile not found '},status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)
# 2.5 DELETE Profile fbv
@api_view(['DELETE'])
def profile_delete(request,pk):
    try:
        profile = Profile.objects.get(id = pk)
        profile.delete()
    except User.DoesNotExist:
        return Response({'error':'profile not found '},status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        return Response({'error':f'error happend {ex}'},status=status.HTTP_400_BAD_REQUEST)

# 3.1 GET POST MIXINS Adresss
class Mixins_Address(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = Address.objects.all()
    serializer_class = AdressSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
# 3.2 GET PUT DELETE MIXINS Adresss
class Mixins_Address_pk(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = Address.objects.all()
    serializer_class = AdressSerializer

    def get(self,request,pk):
        return self.retrieve(request)
    
    def put(self,request,pk):
        return self.update(request)
    
    def delete(self,request,pk):
        return self.destroy(request) 
# 4.1 GET POST Generics PhoneNumber
class Generics_PhoneNumber(generics.ListCreateAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer

# 4.2 GET PUT DELETE Generics PhoneNumber
class Generics_PhoneNumber_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer
