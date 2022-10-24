from __future__ import annotations
import random


class Card:
    numbers = ['3', '4', '5', '6', '7', '8', '9', '10', 'V', 'D', 'R', 'A', '2']

    def __init__(self, number, type):
        self.number: int = number
        self.type: str = type

    def __eq__(self, other: Card):
        return self.numbers.index(self.number) == self.numbers.index(other.number)

    def __gt__(self, other: Card):
        return self.numbers.index(self.number) > self.numbers.index(other.number)

    def __lt__(self, other: Card):
        return self.numbers.index(self.number) < self.numbers.index(other.number)


class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        numbers = ['3', '4', '5', '6', '7', '8', '9', '10', 'V', 'D', 'R', 'A', '2']
        types = ['♥', '♦', '♣', '♠']
        for number in numbers:
            for type in types:
                self.cards.append(Card(number, type))

    def shuffle(self):
        random.shuffle(self.cards)

    def __eq__(self, other: Deck):
        equal = True
        for card1 in self.cards:
            for card2 in self.cards:
                if card1.number != card2.number or card1.type != card2.type:
                    equal = False
        return equal


class Player:

    def __init__(self, name=''):
        self.name = name
        self.hand = []


    def add_to_hand(self, card: Card):
        self.hand.append(card)

    def remove_from_hand(self, card: Card):
        self.hand.remove(card)


player = Player()
player.add_to_hand(Card('3', '♥'))
player.add_to_hand(Card('R', '♥'))
print(len(player.hand))
player.remove_from_hand(Card('3', '♥'))
print(len(player.hand))
