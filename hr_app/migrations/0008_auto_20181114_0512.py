# Generated by Django 2.1.3 on 2018-11-14 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0007_auto_20181114_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('1', 'Open'), ('2', 'HR Reviewed'), ('3', 'Processed')], default='1', max_length=20),
        ),
    ]
