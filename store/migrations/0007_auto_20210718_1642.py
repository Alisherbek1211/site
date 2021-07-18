# Generated by Django 3.2.5 on 2021-07-18 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cupon',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
    ]