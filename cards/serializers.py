from rest_framework import serializers
from django.contrib.auth.models import User
from products.models import Product
from cards.models import Card, Purchase, CardCollection
from products.serializers import ProductSerializer


class CardShowSerializer(serializers.ModelSerializer):
    queryset = Card.objects.all()

    class Meta:
        model = Card
        fields = ['id', 'series', 'number', 'credit',
                  'created', 'activation_status', 'status', 'expiration_months', 'expiration_date']

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


class CardCollectionSerializer(serializers.ModelSerializer):
    queryset = CardCollection.objects.all()

    class Meta:
        model = CardCollection
        fields = ['series', 'credit', 'quantity', 'expiration_months']

    def create(self, validated_data):
        return CardCollection.objects.create(**validated_data)


class PurchaseListSerializer(serializers.ModelSerializer):
    queryset = Purchase.objects.all()
    card = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Card.objects.all())
    product = ProductSerializer(required=False)

    class Meta:
        model = Purchase
        fields = ['id', 'created', 'card', 'product', 'quantity', 'price']

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
        fields = ['id', 'card', 'product', 'quantity', 'created']

    def create(self, validated_data):
        return Purchase.objects.create(**validated_data)


# class CardGeneratorSerializer(serializers.Serializer):
#     series = serializers.CharField(max_length=6)
#     expiration_months = serializers.IntegerField()
#     quantity = serializers.IntegerField()
#     credit = serializers.DecimalField(max_digits=8, decimal_places=2)
