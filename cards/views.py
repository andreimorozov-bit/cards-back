from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, filters
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from cards.models import Card, CardCollection, Purchase
from cards.serializers import (
    CardCollectionSerializer, CardCreateSerializer,
    CardShowSerializer, PurchaseListSerializer, PurchaseCreateSerializer
)
from cards.filters import CardFilter


class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardShowSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_class = CardFilter
    ordering_fields = ['series', 'number',
                       'created', 'status', 'credit', 'expiration_date']
    pagination_class = LimitOffsetPagination

    def get_serializer_class(self):
        serializer_class = CardShowSerializer
        if self.request.method == 'POST':
            serializer_class = CardCreateSerializer
        return serializer_class


class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardShowSerializer

    # def get_serializer_class(self):
    #     serializer_class = CardShowSerializer
    #     if self.request.method == 'POST' or self.request.method == 'PATCH':
    #         serializer_class = CardCreateSerializer
    #     return serializer_class


class PurchaseList(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseListSerializer
    filterset_fields = ['card']

    def get_serializer_class(self):
        serializer_class = PurchaseListSerializer
        if self.request.method == 'POST':
            serializer_class = PurchaseCreateSerializer
        return serializer_class


class PurchaseDetail(generics.DestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseListSerializer


class CreateCards(generics.CreateAPIView):
    queryset = CardCollection.objects.all()
    serializer_class = CardCollectionSerializer
