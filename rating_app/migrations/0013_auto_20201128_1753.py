# Generated by Django 3.1.3 on 2020-11-28 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating_app', '0012_auto_20201128_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='review',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='content_vote',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
        migrations.AlterField(
            model_name='rating',
            name='design_vote',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
        migrations.AlterField(
            model_name='rating',
            name='ux_vote',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
    ]
