# Generated by Django 3.2.7 on 2021-09-29 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyploto_app', '0002_auto_20210928_2333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='datetime',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
