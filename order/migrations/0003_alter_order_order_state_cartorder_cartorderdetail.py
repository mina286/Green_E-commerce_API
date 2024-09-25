# Generated by Django 5.1.1 on 2024-09-22 20:58

import django.db.models.deletion
import django.utils.timezone
import utils.generation_code
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_user'),
        ('products', '0009_product_is_out_of_stock_product_number_of_stock_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_state',
            field=models.CharField(choices=[('recieved', 'recieved'), ('processed', 'processed'), ('shipped', 'shipped'), ('delivered', 'delivered')], max_length=100),
        ),
        migrations.CreateModel(
            name='CartOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=utils.generation_code.generate_code, max_length=20)),
                ('order_state', models.CharField(choices=[('inprogress', 'inprogress'), ('completed', 'completed')], max_length=100)),
                ('order_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('delivery_time', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cartorder_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'cartorder',
                'verbose_name_plural': 'cartorders',
                'db_table': 'CartOrder',
            },
        ),
        migrations.CreateModel(
            name='CartOrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('quantity', models.FloatField()),
                ('cartorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartorderdetail_cartorder', to='order.cartorder')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cartorderdetail_product', to='products.product')),
            ],
            options={
                'verbose_name': 'cartorderdetail',
                'verbose_name_plural': 'cartorderdetails',
                'db_table': 'CartOrderDetail',
            },
        ),
    ]
