import math

class Node():
    def __init__(self, x, y, walkable):
        self.x = x
        self.y = y
        self.walkable = walkable
        #Distance from the starting node
        self.gcost = 0
        #Distance from the end node
        self.hcost = 0
        self.parent = None

    def calculateGCost(self, startingNode):
        """Sets the distance from the node to the starting node
        Diaganols are unit 1.
        """
        xdist = abs(startingNode.x-self.x)
        ydist = abs(startingNode.y-self.y)
        self.gcost = xdist if xdist>ydist else ydist

    def calculateHCost(self, targetNode):
        """sets the distance from the node
        to the targert node. Diagnols are unit 1 as well
        as horizontal and vertical
        """
        xdist = abs(targetNode.x-self.x)
        ydist = abs(targetNode.y-self.y)
        self.hcost = xdist if xdist>=ydist else ydist

    def getFCost(self):
        return self.gcost + self.hcost

    def __str__(self):
        msg = str((self.x, self.y)) + ' '
        msg += 'Walkable: ' + str(self.walkable) + ', '
        msg += 'GCost: ' + str(self.gcost) + ', '
        msg += 'HCost: ' + str(self.hcost) + ', '
        msg += 'FCost: ' + str(self.getFCost())
        return msg

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

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
    targets = []
    for _x in range(minX, maxX+1):
        for _y in range(minY, maxY+1):
            if _x == x and _y == y:
                continue
            coor = (_x, _y)
            targets.append(coor)
    #Now that the targets have been established the path finding can start.
    return targets

def pathfind(x, y, target, board, movespeed, blocks = [' ']):
    """Returns the path to the target, but gives up if movespeed is reached
    uses the A* pathfinding model. 
    """
    openNodes = []
    closedNodes = []
    startNode = Node(x, y, True)
    targetNode = Node(target[0], target[1], True)
    #Leave starting nodes gcost at 0 since it is the starting node
    startNode.calculateHCost(targetNode)
    #Add the starting node to the open nodes
    openNodes.append(startNode)
    while len(openNodes) > 0:
        currentNode = openNodes[0]
        for node in openNodes:
            icost = node.getFCost()
            ccost = currentNode.getFCost()
            if icost < ccost or icost == ccost and node.hcost < currentNode.hcost:
                currentNode = node
        openNodes.remove(currentNode)
        closedNodes.append(currentNode)
        if currentNode.x == targetNode.x and currentNode.y == targetNode.y:
            #Retrace your steps and return the list
            path = retracePath(currentNode)
            return path
        neighbours = getRing(currentNode.x, currentNode.y, 1, board)
        for pathIdx in neighbours:
            #Check if the node is even passable by the player
            fType = str(board[pathIdx])
            walkable = fType not in blocks
            newNode = Node(pathIdx[0], pathIdx[1], walkable)
            newNode.calculateGCost(startNode)
            if not walkable or newNode in openNodes:
                continue
            moveCostToN = currentNode.gcost + getDistance(currentNode, newNode)
            notInList = newNode not in openNodes
            if moveCostToN < newNode.gcost or notInList:
                newNode.gcost = moveCostToN
                newNode.calculateHCost(targetNode)
                newNode.parent = currentNode
                if notInList:
                    openNodes.append(newNode)
            node.calculateGCost(targetNode)
            node.calculateHCost

def getDistance(nodeA, nodeB):
    distX = abs(nodeA.x-nodeB.x)
    distY = abs(nodeA.y-nodeB.y)
    if distX > distY:
        return distX
    else:
        return distY

def retracePath(endNode):
    path = [(endNode.x, endNode.y)]
    previousNode = endNode.parent
    while previousNode is not None:
        coor = (previousNode.x, previousNode.y)
        path.append(coor)
        previousNode = previousNode.parent
    path.reverse()
    return path[1:]

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

    def moveToSquare(self, x, y, board):
        board[x, y].addItemToSquare(self)
        self.x = x
        self.y = y

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
        coor = (self.x, self.y)
        print(coor)
        for target in validTargets:
            #Return the squares indexes to the target
            #will return a shorter array than the target
            #if it was impossible to reach with the move
            #speed allowed.
            path = pathfind(self.x, self.y, target, board, moveSpeed)
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