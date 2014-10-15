class Card():
    min_range = 0
    max_range = 0
    power = 0
    priority = 0
    stun_guard = 3

    def __init__(self, game, player):
        self.game = game
        self.player = player

    # Effects. Override to cause an effect.

    def on_ante(self):
        pass

    def on_reveal(self):
        pass

    def start_of_beat(self):
        pass

    def before_activating(self):
        pass

    def on_hit(self):
        pass

    def on_damage(self):
        pass

    def after_activating(self):
        pass

    def end_of_beat(self):
        pass

class Style(Card):
    pass

class Base(Card):
    pass
