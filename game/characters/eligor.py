class Eligor(Character):
    def __init__(self, game):
        self.unique_base = Aegis(game, self)
        self.styles = [Vengeful(game, self), CounterStyle(game, self), Martial(game, self), Chained(game, self), Retribution(game, self)]
        self.finishers = [ SheetLightning(game, self), SweetRevenge(game, self)]

# Styles

class Vengeful(Style):
    pass
