# Generated by Django 2.1.3 on 2018-11-14 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0004_auto_20181114_0244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_looged_in',
            new_name='is_logged_in',
        ),
    ]