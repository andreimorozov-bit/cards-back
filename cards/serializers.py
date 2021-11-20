from rest_framework import serializers
from django.contrib.auth.models import User
from products.models import Product
from cards.models import Card, Purchase


class CardShowSerializer(serializers.ModelSerializer):
    queryset = Card.objects.all()

    class Meta:
        model = Card
        fields = ['id', 'purchases', 'series', 'number', 'credit',
                  'created', 'status', 'expiration_months', 'expiration_date']

    def create(self, validated_data):
        return Card.objects.create(**validated_data)


class CardCreateSerializer(serializers.ModelSerializer):
    queryset = Card.objects.all()

    class Meta:
        model = Card
        fields = ['series', 'number', 'credit',
                  'activation_status', 'expiration_months']

    def create(self, validated_data):
        return Card.objects.create(**validated_data)


class PurchaseListSerializer(serializers.ModelSerializer):
    queryset = Purchase.objects.all()
    card = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Card.objects.all())
    product = serializers.StringRelatedField(many=False)

    class Meta:
        model = Purchase
        fields = ['id', 'card', 'product', 'quantity', 'price']

    def create(self, validated_data):
        return Purchase.objects.create(**validated_data)


class PurchaseCreateSerializer(serializers.ModelSerializer):
    queryset = Purchase.objects.all()
    card = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Card.objects.all())
    product = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Product.objects.all())

    class Meta:
        model = Purchase
        fields = ['id', 'card', 'product', 'quantity']

    def create(self, validated_data):
        return Purchase.objects.create(**validated_data)


class CardGeneratorSerializer(serializers.Serializer):
    series = serializers.CharField(max_length=6)
    expiration_months = serializers.IntegerField()
    quantity = serializers.IntegerField()
    credit = serializers.DecimalField(max_digits=8, decimal_places=2)
