# Generated by Django 3.2.7 on 2021-10-21 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_alter_order_contact_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='postcode',
            new_name='postal_code',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address',
            new_name='street_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='door_no',
        ),
        migrations.RemoveField(
            model_name='order',
            name='town_or_city',
        ),
    ]
