# Generated by Django 3.2.5 on 2021-07-25 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=255, null=True, verbose_name='Category slug'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='slug',
            field=models.CharField(max_length=255, null=True, verbose_name='Category slug'),
        ),
    ]
