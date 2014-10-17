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
    is_attack = True
    deals_damage = True
    pass

class Strike(Base):
    min_range = 1
    max_range = 1
    power = 4
    priority = 3
    stun_guard = 5

class Shot(Base):
    min_range = 1
    max_range = 4
    power = 3
    priority = 2
    stun_guard = 2

class Grasp(Base):
    min_range = 1
    max_range = 1
    power = 3
    priority = 2
    def on_hit(self):
        self.player.move_opponent(1)

def Drive(Base):
    min_range = 1
    max_range = 1
    power = 3
    priority = 4
    def before_activating(self):
        self.player.advance([1,2])

def Burst(Base):
    min_range = 2
    max_range = 3
    power = 3
    priority = 1
    def start_of_beat(self):
        self.player.retreat([1,2])

def Dash(Base):
    is_attack = False
    power = None
    priority = 9
    def after_activating(self):
        self.player.advance([1,2,3])
        # If switched side, can't get hit.
