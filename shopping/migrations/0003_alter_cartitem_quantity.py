# Generated by Django 3.2.4 on 2021-07-26 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20210726_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveBigIntegerField(default=1),
        ),
    ]
