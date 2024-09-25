from django.urls import path
from . import views

app_name ='accounts'

urlpatterns = [
    path('users/',views.users,name='users'),
    path('signup/',views.signup,name='signup'),
    path('check_code_activate/<int:pk>/',views.check_code_activate,name='check_code_activate'),
    path('user_update/<int:pk>/',views.user_update,name='user_update'),
    path('user_delete/<int:pk>/',views.user_delete,name='user_delete'),
    path('user_detail/<int:pk>/',views.user_detail,name='user_detail'),
    path('change_password/',views.change_password,name='change_password'),
    path('reset_password/',views.reset_password,name='reset_password'),
    # 2.1 GET Profile fbv
    path('profiles/',views.profiles,name='profiles'),
    # 2.2 POST Profile fbv
    path('profile_create/',views.profile_create,name='profile_create'),
    # 2.3 GET Profile fbv
    path('profile_detail/<int:pk>/',views.profile_detail,name='profile_detail'),
    # 2.4 PUT Profile fbv
    path('profile_update/<int:pk>/',views.profile_update,name='profile_update'),
    # 2.5 DELETE Profile fbv
    path('profile_delete/<int:pk>/',views.profile_delete,name='profile_delete'),

    # 3.1 GET POST MIXINS Adresss
    path('Mixins_Address/',views.Mixins_Address.as_view(),name='Mixins_Address'),
    # 3.2 GET PUT DELETE MIXINS Adresss
    path('Mixins_Address_pk/<int:pk>/',views.Mixins_Address_pk.as_view(),name='Mixins_Address_pk'),
    # 4.1 GET POST Generics PhoneNumber
    path('Generics_PhoneNumber/',views.Generics_PhoneNumber.as_view(),name='Generics_PhoneNumber'),
    # 4.2 GET PUT DELETE Generics PhoneNumber
    path('Generics_PhoneNumber_pk/<int:pk>/',views.Generics_PhoneNumber_pk.as_view(),name='Generics_PhoneNumber_pk'),



]
