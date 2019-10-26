import math

def getRing(x, y, offset, board):
    """Gives a list of squares that are valid from the ring offset.
    In this example this would be an x=4, y=4, offset=3. From X, a pathfinder
    does its best to reach each point on the outer ring. Since it takes more
    that the offset to reach the desired ring length, the s's indicate the squares
    that were desired, but unobtainable because of the w walls. This example
    then returns the remaining 22 squares.
    o  o  o  o  o  o  o  o  o  o  o
    o  s  s  m  m  m  m  m  o  o  o
    o  s  o  o  o  o  o  m  o  o  o
    o  m  o  w  w  o  o  m  o  o  o
    o  m  o  w  x  o  o  m  o  o  o
    o  m  o  o  o  o  o  m  o  o  o
    o  m  o  o  o  o  o  m  o  o  o
    o  m  m  m  m  m  m  m  o  o  o
    In this example x=4, y=2 offset=3 which would only return 8 squares
    since the top is sliced off by board threshold, and the w prevents
    the pathfind from finding the outer lower ring.
    o  m  o  o  o  o  o  m  o  o  o
    o  m  o  o  o  o  o  m  o  o  o
    o  m  o  o  x  o  o  m  o  o  o
    o  m  o  w  w  w  w  w  w  w  w
    o  m  o  w  o  o  o  s  o  o  o
    o  s  s  s  s  s  s  s  o  o  o
    o  o  o  o  o  o  o  o  o  o  o
    o  o  o  o  o  o  o  o  o  o  o
    """
    #It has to be assumed the x, y of the character is within the 
    #board.
    minX = x - offset
    if minX < 0:
        minX = 0
    maxX = x + offset
    if maxX > a.shape[0]:
        maxX = a.shape[0]
    minY = y - offset
    if minY < 0:
        minY = 0
    maxY = y + offset
    if maxY > a.shape[1]:
        maxY = a.shape[0]
    #Start with the top left and carry on in a ring.
    for idx in range(x-offset, x+offset+1):
        for idy in range(y-offset, y+offset+1):
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

    def move(self, x, y):
        """Sets the player location to x and y
        """
        self.x = x
        self.y = y

    def checkMovePath(self, board):
        """Checks all the available squares in a board from the current position
        Starts at the player coordinates, checks in a circle around, the continues
        to search circuilar until running out of movement space. Returns a copy of that
        array.
        """
        #Should probably for this player have a list of illegal squares
        #By default, all boards should be surronded by walls at their edges
        #This allows for sloppy array indexing, since we will only go to the edges.
        minX = 1
        minY = 1
        maxX = len(board)-2
        maxY = len(board)-2

        currentSquare = board[self.x, self.y]
        moveSpeed = self.speed
        while moveSpeed > 1:
            topLeft =     board[self.x-1, self.y-1]
            top =         board[self.x+0, self.y-1]
            topRight =    board[self.x+1, self.y-1]
            left =        board[self.x-1, self.y+0]
            right =       board[self.x+1, self.y+0]
            bottomLeft =  board[self.x-1, self.y+1]
            bottom =      board[self.x+0, self.y+1]
            bottomRight = board[self.x+1, self.y+1]
        #When the movement speed is down to 1, the options are limited because you cant
        #end your turn in a spot with a player, boulder, etc

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