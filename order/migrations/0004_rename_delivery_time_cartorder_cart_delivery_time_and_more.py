# Generated by Django 5.1.1 on 2024-09-22 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_order_state_cartorder_cartorderdetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartorder',
            old_name='delivery_time',
            new_name='cart_delivery_time',
        ),
        migrations.RenameField(
            model_name='cartorder',
            old_name='order_state',
            new_name='cart_order_state',
        ),
        migrations.RenameField(
            model_name='cartorder',
            old_name='order_time',
            new_name='cart_order_time',
        ),
        migrations.RenameField(
            model_name='cartorderdetail',
            old_name='cartorder',
            new_name='cart_order',
        ),
    ]
