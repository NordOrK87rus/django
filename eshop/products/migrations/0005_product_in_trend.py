# Generated by Django 2.1.4 on 2018-12-19 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20181219_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_trend',
            field=models.BooleanField(default=False, verbose_name='In trend'),
        ),
    ]
