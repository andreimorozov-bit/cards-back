from django.urls import path
from cards import views

urlpatterns = [
    path('cards/', views.CardList.as_view(), name='card-list'),
    path('cards/<str:pk>/', views.CardDetail.as_view(), name='card-detail'),
    path('purchases/', views.PurchaseList.as_view(), name='purchase-list'),
    path('cards-collection/', views.CreateCards.as_view(), name='create-cards')
]
