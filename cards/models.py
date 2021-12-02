from django.db import models
import uuid
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
from django.utils import timezone
from profiles.models import Profile
from products.models import Product
from random import randrange


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
    series = models.CharField(max_length=7, null=False)
    number = models.CharField(max_length=10, null=False)
    credit = models.DecimalField(max_digits=8, decimal_places=2)
    activation_status = models.CharField(
        max_length=200, choices=STATUS_CHOICES, default=INACTIVE)
    created = models.DateTimeField(auto_now_add=True)
    expiration_months = models.IntegerField(default=1)
    expiration_date = models.DateTimeField(null=True)
    status = models.CharField(
        max_length=200, choices=STATUS_CHOICES, default=INACTIVE)

    def __str__(self):
        return f'{str(self.series)} {str(self.number)}'

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        self.expiration_date = self.created + \
            relativedelta(months=self.expiration_months)
        if self.created + relativedelta(months=self.expiration_months) < timezone.now():
            self.status = self.EXPIRED
        else:
            self.status = self.activation_status

        super(Card, self).save(*args, **kwargs)

    def deduct_from_credit(self, amount):
        self.credit -= amount


class CardCollection(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True,
                          default=uuid.uuid4)
    series = models.CharField(max_length=6)
    expiration_months = models.IntegerField()
    credit = models.DecimalField(max_digits=8, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()

    def save(self, *args, **kwargs):
        for item in range(0, self.quantity):
            new_card = Card(series=self.series,
                            credit=self.credit,
                            expiration_months=self.expiration_months,
                            number=str(randrange(1000000000, 9999999999)),)
            new_card.save()
        super(CardCollection, self).save(*args, **kwargs)


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
        self.price = product.price
        card.deduct_from_credit(product.price * self.quantity)
        product.deduct_from_inventory(self.quantity)
        super(Purchase, self).save(*args, **kwargs)
        card.save()
        product.save()
