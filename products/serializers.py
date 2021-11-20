from rest_framework import serializers
from django.contrib.auth.models import User
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'inventory']

        def create(self, validated_data):
            return Product.objects.create(**validated_data)
