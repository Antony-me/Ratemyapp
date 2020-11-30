# Generated by Django 3.1.3 on 2020-11-30 07:03

import cloudinary.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rating_app', '0017_delete_profilemerch'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileMerch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('bio', models.TextField(blank=True, default='No, bio', max_length=500)),
                ('avatar', cloudinary.models.CloudinaryField(blank=True, default='media/avater.png', max_length=255, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])], verbose_name='image')),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rating_app.post')),
            ],
        ),
    ]
