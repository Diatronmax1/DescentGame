class SkillCard():
    def __init__(self, name, flavorText, ability):
        self.name = name
        self.flavorText = flavorText
        self.ability = ability

class Fighting(SkillCard):
    def __init__(self, name, flavorText, ability):
        super().__init__(name, flavorText, ability)

class Subterfuge(SkillCard):
    def __init__(self, name, flavorText, ability):
        super().__init__(name, flavorText, ability)
        
class Wizardry(SkillCard):
    def __init__(self, name, flavorText, ability):
        super().__init__(name, flavorText, ability)

