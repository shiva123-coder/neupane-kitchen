# Generated by Django 3.2.7 on 2022-02-11 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0017_alter_item_allergen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='chillies',
            field=models.CharField(blank=True, choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four')], default='1', max_length=1, null=True),
        ),
    ]
