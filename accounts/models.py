from django.db import models
from django.contrib.auth.models import User
from settings.models import Country,City
from utils.generation_code import generate_code
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
TYPE_ADDRESS = (
    ('home','home'),
    ('office','office'),
    ('bussiness','bussiness'),
    ('others','others'),

)
TYPE_PHONE = (
    ('primary','primary'),
    ('secondary','secondary'),
   

)
TYPE_ENDER = (
    ('male','male'),
    ('female','female'),
   

)
# 1
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile_user')
    image = models.ImageField(upload_to='profile/',default='/defuser/defuser.png')
    gender = models.CharField(max_length=20,choices=TYPE_ENDER)

    def __str__(self):
        return f"{self.user} "
    class Meta:
        db_table = 'Profile'
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
# 2
class PhoneNumber(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='phonenumber_user')
    phone = models.IntegerField()
    type_phone = models.CharField(max_length=100,choices=TYPE_PHONE,default='primary')

    def __str__(self):
        return f"{self.phone} "
    class Meta:
        db_table = 'PhoneNumber'
        verbose_name = 'phonenumber'
        verbose_name_plural = 'phonenumbers'

# 3
class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='address_user')
    country = models.ForeignKey(Country,on_delete=models.CASCADE,related_name='address_country')
    city = models.ForeignKey(City,on_delete=models.CASCADE,related_name='address_city')
    type_address = models.CharField(max_length=100,choices=TYPE_ADDRESS,default='home')
    state = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    notes = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.street} "
    class Meta:
        db_table = 'Address'
        verbose_name = 'address'
        verbose_name_plural = 'address'

# 4

class ActivationCode(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='activationcode_user')
    code = models.CharField(max_length=20,default=generate_code)
    code_used = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.code}--{self.code_used}"
    class Meta:
        db_table = 'ActivationCode'
        verbose_name = 'ActivationCode'
        verbose_name_plural = 'ActivationCodes'

@receiver(post_save,sender = User)
def create_active_code(sender,instance,created,**kwargs):
    if created :
        ActivationCode.objects.create(user = instance)