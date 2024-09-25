from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import MultipleObjectsReturned

#from django.core.exceptions import MultipleObjectsReturned

class EmailBackend(ModelBackend):
    def authenticate(self, request, username = None , password =None , **kwargs) :
        try:
            print('inside try')
            user = User.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
            print('after tryu')
            print('user====',user)
        except User.DoesNotExist:
            return None     
        except MultipleObjectsReturned :
            print('inside multi object')
            print('MultipleObjectsReturned====',User.objects.filter(email = username).order_by('id').first())
            user = User.objects.filter(email = username).order_by('id').first()
            if user.check_password(password) and self.user_can_authenticate(user):
                    print('check password==',user.check_password(password),"==",self.user_can_authenticate(user))
                    return user
            else :
                 return None
        else:
            print('inside check pass')
            if user.check_password(password) and self.user_can_authenticate(user):
                    print('check password==',user.check_password(password),"==",self.user_can_authenticate(user))
                    return user
           
    def get_user(self, user_id) :
        try:
            return  User.objects.get(id = user_id)
        except User.DoesNotExist:
            return None
        