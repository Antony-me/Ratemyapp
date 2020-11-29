# Generated by Django 3.1.3 on 2020-11-29 11:52

import cloudinary.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating_app', '0014_auto_20201129_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileMerch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('bio', models.TextField(blank=True, default='No, bio', max_length=500)),
                ('projects', models.CharField(blank=True, max_length=100)),
                ('avatar', cloudinary.models.CloudinaryField(blank=True, default='media/avater.png', max_length=255, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])], verbose_name='image')),
            ],
        ),
    ]
