from cards.models import Card
from random import randrange


class CardGenerator():
    @staticmethod
    def generate_cards(series=randrange(100000, 999999),
                       expiration_months=6,
                       quantity=10,
                       credit=10000):
        cards = []
        for item in range(0, quantity):
            cards.append({'series': series,
                          'expiration_months': expiration_months,
                          'number': randrange(1000000000, 9999999999),
                          'credit': credit})
        print(cards)
        return cards
