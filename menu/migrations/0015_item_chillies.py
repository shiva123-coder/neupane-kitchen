# Generated by Django 3.2.7 on 2022-01-24 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0014_item_vegan'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='chillies',
            field=models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four')], default='1', max_length=1, null=True),
        ),
    ]