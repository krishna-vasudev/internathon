# Generated by Django 3.2.3 on 2021-09-25 07:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=120)),
                ('img', models.ImageField(blank=True, upload_to='images/')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('description', models.TextField(blank=True)),
                ('location', models.TextField(blank=True)),
            ],
        ),
    ]
