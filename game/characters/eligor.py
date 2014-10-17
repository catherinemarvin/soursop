class Eligor(Character):
    def __init__(self, game):
        self.unique_base = Aegis(game, self)
        self.styles = [Vengeful(game, self), CounterStyle(game, self), Martial(game, self), Chained(game, self), Retribution(game, self)]
        self.finishers = [ SheetLightning(game, self), SweetRevenge(game, self)]

# Styles

class Vengeful(Style):
    min_range = 0
    max_range = 0
    power = 1
    priority = 0
    stun_guard = 3

    def before_activating(self):
        self.player.advance(1)

    def on_hit(self):
        self.player.change_tokens(2)

class Retribution(Style):
    min_range = 0
    max_range = 0
    power = 0
    priority = -1
    soak = 2

class Counter(Style):
    min_range = 0
    max_range = 0
    power = 1
    priority = -1

    def start_of_beat(self):
        if self.player.base.name == self.player.opponent.base.name:
            self.player.opponent.stun()

    def before_activating(self):
        if self.player.damage_taken > 0:
            self.player.advance(range(self.player.damage_taken + 1))

class Martial(Style):
    min_range = 0
    max_range = 1
    power = 1
    priority = -1

    def before_activating(self):
        if self.player.damage_taken > 0:
            self.player.add_power(2)
        if self.player.tokens == 5:
            self.player.add_power(2)

class Chained(Style):
    min_range = 0
    max_range = 0
    priority = -1

    def before_activating(self):
        # Pull the opponent one space per token discarded.


class Aegis(Base):
    min_range = 1
    max_range = 1

    @property
    def power(self):
        if self.player.opponent.base.printed_power is None:
            return 0
        else:
            return self.opponent.style.printed_power + self.opponent.base.printed_power
