class Game:
    """A representation of a BattleCon game"""
    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2

        self.waiting_for_character1 = True
        self.waiting_for_character2 = True

    def receive_move(style, base, character):
        if character == character1:
            self.waiting_for_character1 = False
        elif character == character2:
            self.waiting_for_character2 = False
        else:
            print "Something has gone terribly wrong"
