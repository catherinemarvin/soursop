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

