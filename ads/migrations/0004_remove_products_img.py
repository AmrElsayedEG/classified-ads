# Generated by Django 2.1 on 2019-01-29 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_auto_20190129_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='img',
        ),
    ]
