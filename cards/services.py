from cards.models import Card
from random import randrange


class CardGenerator():
    @staticmethod
    def generate_cards(series=str(randrange(100000, 999999)),
                       expiration_months=6,
                       quantity=10,
                       credit=10000):

        for item in range(0, quantity):
            new_card = Card(series=str(series),
                            credit=credit,
                            expiration_months=expiration_months,
                            number=str(randrange(1000000000, 9999999999)),)
            new_card.save()
        return quantity
