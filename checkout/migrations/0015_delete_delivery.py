# Generated by Django 3.2.7 on 2022-02-28 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0014_delivery'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Delivery',
        ),
    ]