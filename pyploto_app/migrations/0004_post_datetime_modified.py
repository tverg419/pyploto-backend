# Generated by Django 3.2.7 on 2021-10-03 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyploto_app', '0003_auto_20211002_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='datetime_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
