# Generated by Django 3.2.5 on 2021-07-29 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_remove_cartitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveBigIntegerField(default=1, null=True),
        ),
    ]