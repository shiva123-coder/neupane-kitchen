# Generated by Django 3.2.7 on 2022-03-01 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0017_auto_20220301_1445'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
