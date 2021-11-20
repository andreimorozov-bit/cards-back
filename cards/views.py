from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, permissions, renderers
from cards.models import Card, Purchase
from cards.serializers import CardCreateSerializer, CardGeneratorSerializer, CardShowSerializer, PurchaseListSerializer, PurchaseCreateSerializer
from cards.services import CardGenerator


class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardShowSerializer

    def get_serializer_class(self):
        serializer_class = CardShowSerializer
        if self.request.method == 'POST':
            serializer_class = CardCreateSerializer
        return serializer_class


class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardShowSerializer

    def get_serializer_class(self):
        serializer_class = CardShowSerializer
        if self.request.method == 'POST' or self.request.method == 'PATCH':
            serializer_class = CardCreateSerializer
        return serializer_class


class PurchaseList(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseListSerializer
    filterset_fields = ['card']

    def get_serializer_class(self):
        serializer_class = PurchaseListSerializer
        if self.request.method == 'POST':
            serializer_class = PurchaseCreateSerializer
        return serializer_class


class CreateCards(generics.CreateAPIView):
    serializer_class = CardGeneratorSerializer

    def create(self, request, *args, **kwargs):
        cards = CardGenerator.generate_cards(series=request.query_params['series'],
                                             quantity=request.query_params['quantity'],
                                             expiration_months=request.query_params['expiration_months'],
                                             credit=request.query_params['credit'])
        for item in cards:
            new_card = Card(series=item['series'],
                            quantity=item['quantity'],
                            credit=item['credit'],
                            expiration_months=item['expiration_months'])
            new_card.save()

        return Response(status=201)
