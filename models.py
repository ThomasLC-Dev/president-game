class Card:
    def __init__(self, number, type):
        self.number: int = number
        self.type: str = type


class Deck:
    def __init__(self):
        self.cards = []
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'V', 'D', 'R', 'A']


    def shuffle(self):
        pass