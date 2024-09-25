from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} "
    class Meta:
        db_table = 'Country'
        verbose_name = 'country'
        verbose_name_plural = 'countries'


class City(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE,related_name='city_country')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} "
    class Meta:
        db_table = 'City'
        verbose_name = 'city'
        verbose_name_plural = 'cities'