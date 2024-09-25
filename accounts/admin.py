from django.contrib import admin
from .models import Profile,PhoneNumber,Address,ActivationCode
# Register your models here.
# 2
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_display_links = ['user']
admin.site.register(Profile,ProfileAdmin)
# 2
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ['user','phone','type_phone']
    list_display_links = ['user','phone','type_phone']
admin.site.register(PhoneNumber,PhoneNumberAdmin)
# 3
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user','country','city','type_address','street']
    list_display_links = ['user','country','city','type_address','street']
admin.site.register(Address,AddressAdmin)

# 4
class ActivationCodeAdmin(admin.ModelAdmin):
    list_display = ['user_id','user','code','code_used']
    list_display_links = ['user_id','user','code','code_used']
admin.site.register(ActivationCode,ActivationCodeAdmin)