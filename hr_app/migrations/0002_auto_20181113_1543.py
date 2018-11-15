# Generated by Django 2.1.3 on 2018-11-13 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[(1, 'NORMAL'), (2, 'HR'), (3, 'MANAGER')], default=1, max_length=100),
        ),
        migrations.AddField(
            model_name='request',
            name='processor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='request_request_processor_id', to='hr_app.User'),
        ),
        migrations.AddField(
            model_name='request',
            name='requester_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_requester_id', to='hr_app.User'),
        ),
    ]
