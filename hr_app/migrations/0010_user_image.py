# Generated by Django 2.1.3 on 2018-11-14 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0009_auto_20181114_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.BinaryField(blank=True),
        ),
    ]
