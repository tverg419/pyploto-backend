# Generated by Django 3.2.7 on 2021-09-29 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyploto_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='author_id',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='post_id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='datetime',
        ),
    ]
