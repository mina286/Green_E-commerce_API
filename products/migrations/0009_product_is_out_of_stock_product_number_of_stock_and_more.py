# Generated by Django 5.1.1 on 2024-09-20 16:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_is_sale_product_sale_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_out_of_stock',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='number_of_stock',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddConstraint(
            model_name='product',
            constraint=models.CheckConstraint(condition=models.Q(('number_of_stock__gte', 0)), name='number_of_stock__gte0'),
        ),
    ]
