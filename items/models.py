from django.db import models

# Create your models here.
from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.item_name