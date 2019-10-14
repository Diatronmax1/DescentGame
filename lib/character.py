class CharacterSheet():
    def __init__(self, name, 
                 health=0, 
                 fatigue=0, 
                 armor=0, 
                 speed=0, 
                 meleeTrait=0, 
                 rangeTrait=0, 
                 magicTrait=0, 
                 fightingSkill=0, 
                 subterfugeSkill=0, 
                 wizardrySkill=0, 
                 conquestValue=0):
        self.name = name
        self.health = health
        self.fatigue = fatigue
        self.armor = armor
        self.speed = speed
        self.meleeTrait = meleeTrait
        self.rangeTrait = rangeTrait
        self.magicTrait = magicTrait
        self.ability = None
        self.fightingSkill = fightingSkill
        self.subterfugeSkill = subterfugeSkill
        self.wizardrySkill = wizardrySkill
        self.conquestValue = conquestValue
        #Visuals
        self.playerModel = None

    def setHealth(self, health):
        self.health = health

    def setFatigue(self, fatigue):
        self.fatigue = fatigue