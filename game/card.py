class Card():
    min_range = 0
    max_range = 0
    power = 0
    priority = 0

    def __init__(self, game, player):
        self.game = game
        self.player = player

class Style(Card):
    pass

class Base(Card):
    pass
