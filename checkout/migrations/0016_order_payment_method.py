# Generated by Django 3.2.7 on 2022-03-01 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0015_delete_delivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('card', 'card'), ('cash', 'cash')], default='card', max_length=10),
        ),
    ]
