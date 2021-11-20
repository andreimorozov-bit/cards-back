from django.db import models
import uuid


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    title = models.CharField(max_length=500, default='')
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    inventory = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    def deduct_from_inventory(self, amount):
        self.inventory -= amount
