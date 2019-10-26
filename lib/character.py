import math

def getRing(x, y, offset, board):
    """Returns all squares in a square based on an offset,
    avoids going past board edges.
    """
    #Board limits.
    minX = x - offset
    if minX < 0:
        minX = 0
    maxX = x + offset
    if maxX > board.shape[0]:
        maxX = board.shape[0]
    minY = y - offset
    if minY < 0:
        minY = 0
    maxY = y + offset
    if maxY > board.shape[1]:
        maxY = board.shape[0]
    targets = [(x, y) for x in range(minX, maxX+1) for y in range(minY, maxY+1)]
    #Now that the targets have been established the path finding can start.
    return targets

def pathfind(x, y, target, movespeed):
    """Returns the path to the target, but gives up if movespeed is reached
    uses the A* pathfinding model. 
    Adds the starting node to the OPEN list, calculates
    g cost = distance from starting node
    h cost = distance from ending node
    f cost = g cost + h cost
    """
    pass

class Character():
    def __init__(self, characterSheet):
        self.name = characterSheet.name
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
        for effect in self.statusEffects.values():
            effect.affect(self)
            if self.health <= 0:
                self.die()
                return
        for item in self.bag:
            item.refresh()

    def equipItems(self):
        print('can equip ' + str(self.bag))

    def chooseAction(self):
        print('Choose an action\n0: Run\n1: Battle\n2: Advance\n3:Ready')

    def run(self):
        return self.speed*2

    def move(self, x, y):
        """Sets the player location to x and y
        """
        self.x = x
        self.y = y

    def checkMovePath(self, moveSpeed, board):
        """Checks all the available squares in a board from the current position
        Starts at the player coordinates, checks in a circle around, the continues
        to search circuilar until running out of movement space. Returns a copy of that
        array.
        """
        #Gather a list of targets which is the maximum move speed the player has
        targets = getRing(self.x, self.y, moveSpeed, board)
        #print(targets)
        validTargets = [target for target in targets if str(board[target]) == 'F']
        print(validTargets)
        for target in validTargets:
            #Return the squares indexes to the target
            #will return a shorter array than the target
            #if it was impossible to reach with the move
            #speed allowed.
            path = pathfind(self.x, self.y, target, moveSpeed)
            print(target)
            print(path)

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