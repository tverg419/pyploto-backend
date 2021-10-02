# Generated by Django 3.2.7 on 2021-10-02 22:59

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyploto_app', '0002_auto_20210929_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='media',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
