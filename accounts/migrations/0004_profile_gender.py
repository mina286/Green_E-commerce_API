# Generated by Django 5.1.1 on 2024-09-22 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_activationcode_code_used_alter_activationcode_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('Female', 'Female')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
