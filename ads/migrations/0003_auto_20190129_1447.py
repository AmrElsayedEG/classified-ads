# Generated by Django 2.1 on 2019-01-29 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_auto_20190129_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
