from __future__ import annotations
import random


class Card:
    numbers = ['3', '4', '5', '6', '7', '8', '9', '10', 'V', 'D', 'R', 'A', '2']

    def __init__(self, number: str, type: str):
        self.number: str = number
        self.type: str = type

    def __eq__(self, other: Card):
        return self.numbers.index(self.number) == self.numbers.index(other.number)

    def __gt__(self, other: Card):
        return self.numbers.index(self.number) > self.numbers.index(other.number)

    def __ge__(self, other: Card):
        return self.numbers.index(self.number) >= self.numbers.index(other.number)

    def __lt__(self, other: Card):
        return self.numbers.index(self.number) < self.numbers.index(other.number)

    def __le__(self, other: Card):
        return self.numbers.index(self.number) <= self.numbers.index(other.number)


class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        numbers = Card.numbers
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
        if(self.name == ''):
            self.name = "Player " + str(random.randrange(1, 100))

    def add_to_hand(self, card: Card):
        if len(self.hand) == 0:
            print(card.number + card.type)
            self.hand.append(card)
        else:
            for cardInHandIndex, cardInHand in enumerate(self.hand):
                if cardInHand >= card:
                    self.hand.insert(cardInHandIndex, card)
                    break
                elif cardInHandIndex == len(self.hand) - 1:
                    self.hand.append(card)
                    break


    def remove_from_hand(self, card: Card):
        self.hand.remove(card)

    def play(self, numberOfCards, lastValueOfCards):
        print(self.name + " - Play")
        self.show_hand()

        wantToPlay = input("Désirez-vous passer votre tour : ")
        if wantToPlay == "Y":
            return None


        availableCards = []
        while(len(availableCards) < int(numberOfCards)):
            availableCard = []
            valueOfCards = input("Valeur des cartes : ")
            if Card(valueOfCards, '') >= Card(lastValueOfCards, ''):
                for card in self.hand:
                    if card.number == valueOfCards and len(availableCards) < int(numberOfCards):
                        availableCards.append(card)
            else:
                print("Valeur de carte insuffisante")


        for removedCard in availableCards:
            self.remove_from_hand(removedCard)

        print("Vous avez joué : " + valueOfCards)
        return valueOfCards

    def show_hand(self):
        cardsValue = []
        for card in self.hand:
            cardsValue.append(card.number+card.type)

        print("[" + ",".join(cardsValue) + "]")

    def __eq__(self, other: Player):
        return self.name == other.name


class AIPlayer(Player):
    pass


class PresidentGame:
    def __init__(self, players: []):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = players
        self.distribute_cards()

    def distribute_cards(self):
        indexPlayer = 0
        for card in self.deck.cards:
            if indexPlayer >= len(self.players):
                indexPlayer = 0

            self.players[indexPlayer].add_to_hand(card)
            indexPlayer += 1


class Trick:
    def __init__(self):
        self.numberOfCards = 0
        self.lastValueOfCards = '3'
        self.lastPlayer = None
