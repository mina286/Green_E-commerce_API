# Generated by Django 5.1.1 on 2024-09-25 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_coupon_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_fee',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
