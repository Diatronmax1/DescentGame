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
                 conquestValue=0,
                 expansion='base'):
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
        self.expansion = 'base'
        #Visuals
        self.playerModel = None

    def setParam(self, paramName, value):
        msg = ''
        if paramName in self.__dict__:
            #Will only allow values like 0, 12, 22, 8. negative is not allowed.
            if type(value) == str:
                if value.isdigit():
                    setattr(self, paramName, int(value))
                else:
                    try:
                        setVal = float(value)
                        if setVal >= 0:
                            setattr(self, paramName, round(setVal))
                        else:
                            msg = 'Value: ' + str(setVal) + ' must be >= 0'
                    except:
                        msg = 'Cant convert ' + value + ' to int >= 0'
            elif type(value) == int:
                if value >= 0:
                    setattr(self, paramName, value)
                else:
                    msg = 'Value ' + str(value) + ' cannot be < 0'
            else:
                try:
                    value = round(value)
                    if value >= 0:
                        setattr(self, paramName, value)
                    else:
                        msg = 'Value ' + str(value) + ' cannot be < 0'
                except:
                    msg = str(value) + ' cannot be added as a health value.'
        else:
            msg = paramName + ' not in Character Sheet, cant modify'
        return msg

    def __str__(self):
        rtmsg = 'Name: ' + self.name + '\n'
        rtmsg += 'Health: ' + str(self.health) + '\n'
        rtmsg += 'Fatigue: ' + str(self.fatigue) + '\n'
        rtmsg += 'Armor: ' + str(self.armor) + '\n'
        rtmsg += 'Speed: ' + str(self.speed) + '\n'
        rtmsg += 'Melee Trait: ' + str(self.meleeTrait) + '\n'
        rtmsg += 'Range Trait: ' + str(self.rangeTrait) + '\n'
        rtmsg += 'Magic Trait: ' + str(self.magicTrait) + '\n'
        rtmsg += 'Hero Ability: ' + str(self.ability) + '\n'
        rtmsg += 'Fighting Skill: ' + str(self.fightingSkill) + '\n'
        rtmsg += 'Subterfuge Skill: ' + str(self.subterfugeSkill) + '\n'
        rtmsg += 'Wizardry Skill: ' + str(self.wizardrySkill) + '\n'
        rtmsg += 'Conquest Value: ' + str(self.conquestValue) +'\n'
        rtmsg += 'From Game: ' + self.expansion + '\n'
        return rtmsg