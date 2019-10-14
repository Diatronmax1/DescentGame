class Item():
    def __init__(self, ability, value. cursed=False):
        self.ability = ability
        self.goldvalue = goldvalue

class Weapon(Item):
    def __init__(self, ability, attackType, hands, dice, value, cursed=False):
        super().__init__(ability, value, cursed)
        self.hands = hands
        self.attackType
        self.dice = dice

class Relic(Weapon):
    def __init__(self, ablity, attackType, hands, dice, value, cursed=False):
        super().__init__(ability, hands, dice, value, cursed)

class Armor(Item):
    def __init__(self, ability, value, cursed=False):
        super().__init__(ability, value, cursed)

class Other(Item):
    def __init__(self, ability, value, cursed=False):
        super().__init__(ability, value, cursed)

class Shield(Item):
    def __init__(self, ability, value, cursed=False):
        super().__init__(self, ability, value. cursed)