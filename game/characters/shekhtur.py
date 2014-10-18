class Shekhtur(Character):
    def __init__(self, game):
        self.unique_base = Brand(game, self)
        self.styles = [ Unleashed(game, self), Reaver(game, self), Combination(game, self), Jugular(game, self), Spiral(game, self) ]
        self.finishers = [ SoulBreaker(game, self), CoffinNails(game, self)]

# Styles

class Unleashed(Style):
    min_range = 0
    max_range = 1
    power = -1
    priority = 0

    def after_activating(self):
        self.player.retreat([1,2])

    def end_of_beat(self):
        self.player.gain_tokens(2)
        self.player.next_beat_power(1)

class Reaver(Style):
    min_range = 0
    max_range = 1
    power = 0
    priority = 0

    def on_damage(self):
        self.player.push(self.damage)

    def end_of_beat(self):
        self.player.advance([1,2])

class Combination(Style):
    min_range = 0
    max_range = 0
    power = 2
    priority = 0

    # Does not hit at range 3 or greater
    # Ignores soak at 7 or greater

    def on_hit(self):
        if self.hit_opponent_last_beat:
            self.player.power(2)

class Jugular(Style):
    min_range = 0
    max_range = 0
    power = 1
    priority = 2

    def on_hit(self):
        self.opponent.move(1)

    def end_of_beat(self):
        self.player.tokens = 3

class Spiral(Style):
    min_range = 0
    max_range = 0
    power = -1

    def before_activating(self):
        # Advance up to 3 spaces, - 1 power for each space moved.
