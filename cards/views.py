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
        print(request.query_params)
        print(kwargs)
        cards = CardGenerator.generate_cards(series=str(request.query_params['series']),
                                             quantity=int(
                                                 request.query_params['quantity']),
                                             expiration_months=int(
                                                 request.query_params['expiration_months']),
                                             credit=float(request.query_params['credit']))

        response = f'{cards} cards created'

        return Response(response, status=201)
