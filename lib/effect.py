class Effect():
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def stack(self, stackVal):
        self.strength += stackVal

class Burn(Effect):
    def __init__(self, name, strength):
        super().__init__(name, strength)

    def affect(self, character):
        character.health -= self.strength