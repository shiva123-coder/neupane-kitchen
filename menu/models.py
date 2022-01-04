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
        ('Sulphur Dioxide/Sulphite', 'Sulphur Dioxide/Sulphite')   
    )


class Item(models.Model):
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=170)
    heading = models.TextField(max_length=150, null=True, blank=True)
    description = models.TextField(max_length=270, null=True, blank=True)
    allergen = MultiSelectField(
        choices=ALLERGEN_CHOICES, null=True, blank=False)
    note = models.TextField(max_length=80, null=True, blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
