# Generated by Django 3.2.5 on 2021-07-18 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20210718_1642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='icon',
            new_name='image',
        ),
    ]