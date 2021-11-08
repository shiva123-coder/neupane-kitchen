from django.db import models


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


class Item(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    tag = models.CharField(max_length=170, null=True, blank=True)
    name = models.CharField(max_length=170)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
