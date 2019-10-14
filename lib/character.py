import math

class Character():
    def __init__(self, characterSheet):
        self.default = characterSheet
        self.health = characterSheet.health
        #Depending on the items a character has health could be modded
        self.healthMod = 0
        self.fatigue = characterSheet.fatigue
        self.fatigueMod = 0
        self.armor = characterSheet.armor
        self.armorMod = 0
        self.speed = characterSheet.speed
        self.speedMod = 0
        #Stuff
        self.money = 0
        self.bag = {}
        self.statusEffects = {}
        self.mapLocation = 'town'
        self.x = 0
        self.y = 0
        self.heroOrder = None

    def refreshCards(self):
        """Start of a players turn, all status effects will take effect here
        """
        for effect in self.statusEffects.value():
            effect.affect(self)
            if self.health <= 0:
                self.die()
                return
        for item in self.bag:
            item.refresh()

    def equipItems(self):
        print('can equip ' + str(self.bag))

    def run(self):
        return self.speed*2

    def move(self, x, y):
        """Sets the player location to x and y
        """
        self.x = x
        self.y = y

    def attack(self, weaponName):
        currentWeapon = self.bag[weaponName]
        return currentWeapon.dice

    def ready(self, orderChoice):
        self.heroOrder = orderChoice

    def takeDamage(self, damage, pierce=0, effects={}):
        effectiveArmor = self.armor-pierce
        if damage > effectiveArmor:
            self.health = self.health - (damage-effectiveArmor)
            if self.health <= 0:
                return self.die()
            for effect in effects:
                if effect in self.statusEffects:
                    self.statusEffects[effect.name].stack(effect.strength)
                else:
                    self.statusEffects[effect.name] = effect

    def die(self):
        """Dying places the character in town
        restores their health and fatigue and
        removes half of their money rounded up
        and removes all status effects
        """
        self.health = self.default.health + self.healthMod
        self.fatigue = self.default.fatigue + self.fatigueMod
        self.money = math.ceil(self.money/25/2)*25
        self.statusEffects.clear()
        self.mapLocation = 'town'
        #Return the characters value
        return self.default.conquestValue