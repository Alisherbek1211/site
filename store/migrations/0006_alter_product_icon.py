# Generated by Django 3.2.5 on 2021-07-18 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='icon',
            field=models.ImageField(null=True, upload_to='image/', verbose_name='images'),
        ),
    ]
