class Skill():
    def __init__(self, name, flavorText, ability):
        self.name = name
        self.flavorText = flavorText
        self.ability = ability

class Fighting(Skill):
    def __init__(self, name, flavorText, ability):
        super().__init__(name, flavorText, ability)

class Subterfuge(Skill):
    def __init__(self, name, flavorText, ability):
        super().__init__(name, flavorText, ability)

class Wizardry(Skill):
    def __init__(self, name, flavorText, ability):
        super().__init__(name, flavorText, ability)

