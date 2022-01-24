from django.db import models
from multiselectfield import MultiSelectField


class Category(models.Model):
    """ Model for stock categories """

    class Meta:
        """
        adjust the spelling of categories.
        override django from adding s to the model name.
        """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=170)
    display_name = models.CharField(max_length=170, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


ALLERGEN_CHOICES = (
        ('Celery', 'Celery'),
        ('Cereals containing gluten', 'Cereals containing gluten'),
        ('Crustaceans', 'Crustaceans'),
        ('Egg', 'Egg'),
        ('Fish', 'Fish'),
        ('Lupin', 'Lupin'),
        ('Milk', 'Milk'),
        ('Molluscs', 'Molluscs'),
        ('Mustard', 'Mustard'),
        ('Tree nuts/Nuts', 'Tree nuts/Nuts'),
        ('Peanuts', 'Peanuts'),
        ('Sesame Seeds', 'Sesame Seeds'),
        ('Soya', 'Soya'),
        ('Sulphur Dioxide/Sulphite', 'Sulphur Dioxide/Sulphite'),
        ('None', 'None'),
    )


class Item(models.Model):
    CHILLI_CHOICES = (
        ("1", "One"),
        ("2", "Two"),
        ("3", "Three"),
        ("4", "Four"),
    )
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=170)
    chillies = models.CharField(
        choices=CHILLI_CHOICES, default='1', max_length=1,  null=True, blank=False)
    heading = models.TextField(max_length=250, null=True, blank=True)
    description = models.TextField(max_length=370, null=True, blank=True)
    ingredient = models.TextField(max_length=700, null=True, blank=True)
    vegan = models.BooleanField(null=True, blank=False)
    allergen = MultiSelectField(
        choices=ALLERGEN_CHOICES, null=True, blank=False)
    note1 = models.TextField(max_length=280, null=True, blank=True)
    note2 = models.TextField(max_length=280, null=True, blank=True)
    note3 = models.TextField(max_length=280, null=True, blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
