# Generated by Django 2.1 on 2019-01-29 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_products_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='img',
            field=models.ImageField(blank=True, default='default.bmp', upload_to='product_img'),
        ),
    ]