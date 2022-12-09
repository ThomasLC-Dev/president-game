from __future__ import annotations
import random


class Card:
    """
    Card class
    Use to store information about each card
    """
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
    """
    Deck class
    Use to create the deck of cards
    """

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
    """
    Player class
    Use to store user information, and allow player to show him hand and to play
    """

    def __init__(self, name='', role=''):
        self.name = name
        self.role = role
        self.hand = []
        if (self.name == ''):
            self.name = "Joueur " + str(random.randrange(1, 100))

    def add_to_hand(self, card: Card):
        if len(self.hand) == 0:
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

    def play(self, number_of_cards, last_value_of_cards):
        print(self.name + " - Joue")
        self.show_hand()
        print(
            "Vous devez jouer " + str(number_of_cards) + " cartes d'une valeur minimum de " + last_value_of_cards + ".")

        skip_play = input("Désirez-vous passer votre tour (Y/Entrée) : ")
        if skip_play == "Y":
            return None

        available_cards = []
        while len(available_cards) < int(number_of_cards):
            if len(available_cards) != 0:
                print("Nombre de carte insuffisant")

            available_cards = []
            value_of_cards = input("Valeur des cartes (X pour quitter) : ")
            if value_of_cards == "X":
                return None
            elif value_of_cards in Card.numbers and Card(value_of_cards, '') >= Card(last_value_of_cards, ''):
                for card in self.hand:
                    if card.number == value_of_cards and len(available_cards) < int(number_of_cards):
                        available_cards.append(card)
            else:
                print("Valeur de carte insuffisante")

        for removed_card in available_cards:
            self.remove_from_hand(removed_card)

        print("Vous avez joué : " + value_of_cards)
        return value_of_cards

    def show_hand(self):
        cards_value = []
        for card in self.hand:
            cards_value.append(card.number + card.type)

        print("[" + ",".join(cards_value) + "]")

    def select_number_of_cards(self):
        self.show_hand()
        number_of_cards = ""
        is_not_between_1_and_4 = True
        while is_not_between_1_and_4:
            number_of_cards = input("Vous êtes le premier joueur, veuillez indiquer le nombre de cartes du tour : ")
            try:
                if 0 < int(number_of_cards) < 5:
                    is_not_between_1_and_4 = False
            finally:
                continue

        return number_of_cards

    def __eq__(self, other: Player):
        return self.name == other.name


class AIPlayer(Player):
    """
    AI Player class extends from Player
    Artificial Intelligence Player to replace real player
    """

    def __init__(self):
        self.name = "Joueur IA " + str(random.randrange(1, 100))
        super().__init__(self.name)

    def play(self, number_of_cards, last_value_of_cards):
        print(self.name + " - Joue")

        available_cards = []
        value_of_cards = last_value_of_cards
        while len(available_cards) < int(number_of_cards):
            available_cards = []
            for card in self.hand:
                if card.number == value_of_cards and len(available_cards) < int(number_of_cards):
                    available_cards.append(card)

            if len(available_cards) >= int(number_of_cards):
                break
            elif value_of_cards == "2":
                return None
            else:
                value_of_cards = Card.numbers[Card.numbers.index(value_of_cards) + 1]

        for removed_card in available_cards:
            self.remove_from_hand(removed_card)

        print(self.name + " a joué " + str(len(available_cards)) + " cartes de valeur " + value_of_cards)
        return value_of_cards

    def select_number_of_cards(self):
        return random.randrange(1, 5)


class PresidentGame:
    """
    PresidentGame class
    Use to store, shuffle and distribute the deck
    """

    def __init__(self, players: []):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = players
        self.distribute_cards()

    def distribute_cards(self):
        index_player = 0
        for card in self.deck.cards:
            if index_player >= len(self.players):
                index_player = 0

            self.players[index_player].add_to_hand(card)
            index_player += 1


class Trick:
    """
    Trick class
    Use to store every information about the current trick
    """

    def __init__(self):
        self.number_of_cards = 0
        self.last_value_of_cards = '3'
        self.last_player = None
