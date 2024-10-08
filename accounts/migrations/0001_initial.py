# Generated by Django 5.1.1 on 2024-09-20 17:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('settings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_address', models.CharField(choices=[('home', 'home'), ('office', 'office'), ('bussiness', 'bussiness'), ('others', 'others')], default='home', max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('notes', models.CharField(max_length=200)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address_city', to='settings.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address_country', to='settings.country')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'address',
                'db_table': 'Address',
            },
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('type_phone', models.CharField(choices=[('primary', 'primary'), ('secondary', 'secondary')], default='primary', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phonenumber_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'phonenumber',
                'verbose_name_plural': 'phonenumbers',
                'db_table': 'PhoneNumber',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='/defuser/defuser.png', upload_to='profile/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
                'db_table': 'Profile',
            },
        ),
    ]
