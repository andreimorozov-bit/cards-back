from django.db import models
import uuid
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
from django.utils import timezone
from profiles.models import Profile
from products.models import Product


class Card(models.Model):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    EXPIRED = 'EXPIRED'
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
        (EXPIRED, 'Expired'),
    )

    id = models.UUIDField(primary_key=True, editable=False, unique=True,
                          default=uuid.uuid4)
    owner = models.ForeignKey(
        Profile, null=True, on_delete=models.SET_NULL, related_name='cards')
    series = models.CharField(max_length=6, null=False)
    number = models.CharField(max_length=10, null=False)
    credit = models.DecimalField(max_digits=8, decimal_places=2)
    activation_status = models.CharField(
        max_length=200, choices=STATUS_CHOICES, default=INACTIVE)
    created = models.DateTimeField(auto_now_add=True)
    expiration_months = models.IntegerField(default=1)

    @property
    def expiration_date(self):
        return self.created + relativedelta(months=self.expiration_months)

    @property
    def status(self):
        if self.created + relativedelta(months=self.expiration_months) < timezone.now():
            return self.EXPIRED
        else:
            return self.activation_status

    def __str__(self):
        return f'{str(self.series)} {str(self.number)}'

    def deduct_from_credit(self, amount):
        self.credit -= amount


class Purchase(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True,
                          default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    card = models.ForeignKey(
        Card, on_delete=models.SET_NULL, null=True, related_name='purchases')
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, related_name='purchases')
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        product = self.product
        card = self.card
        self.price = product.price * self.quantity
        card.deduct_from_credit(product.price * self.quantity)
        product.deduct_from_inventory(self.quantity)
        super(Purchase, self).save(*args, **kwargs)
        card.save()
        product.save()
