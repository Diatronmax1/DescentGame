#Imports
import os, pickle, numpy as np
from . import charactersheet
from .overlord import Overlord
from . import square

def query(queryMsg, acceptedMsgs = []):
    moveon = False
    while not moveon:
        x = input(queryMsg)
        if acceptedMsgs:
            if x in acceptedMsgs:
                return x
            else:
                print(x + ' not valid, accepted: ' + str(acceptedMsgs))
        else:
            return x

class DescentGame():
    def __init__(self, numPlayers):
        self.numPlayers = numPlayers
        self.characterDir = os.path.join(os.path.dirname(__file__), 'characters/')
        self.mapDir = os.path.join(os.path.dirname(__file__), 'maps/')
        self.loadSavedMaps(self.mapDir)
        self.savedCharNames = self.loadSavedCharacters(self.characterDir)
        self.characters = {}
        #In game stuff
        self.currentRound = 0

    def loadSavedMaps(self, mapDir):
        print('Loading available maps from ' + mapDir)

    def loadSavedCharacters(self, charDir):
        return {f:None for f in os.listdir(self.characterDir)}

    def selectCharacter(self, charName):
        if charName in self.savedCharNames:
            with open(os.path.join(self.characterDir, charName), 'rb') as bFile:
                newChar = pickle.load(bFile)
                self.characters[charName] = newChar
        else:
            print(charName + ' not in saved characters')

    def loadBoard(self, boardPath):
        print('loading board')
        self.board = np.empty((20,20), dtype=object)
        for x in range(20):
            for y in range(20):
                newSquare = square.Wall()
                self.board[x, y] = newSquare
        self.board[0,0] = square.Floor()
        self.board[0,1] = square.Floor()
        self.board[1,0] = square.Floor()
        self.board[1,1] = square.Floor()
        for y in range(20):
            self.board[2,y] = square.Floor()
            self.board[3,y] = square.Floor()
            if y > 2 and y < 17:
                self.board[9,y]=square.Floor()
                self.board[10,y]=square.Floor()
        for x in range(4, 11):
            self.board[x,14] = square.Floor()
            self.board[x,15] = square.Floor()
            self.board[x,16] = square.Floor()
            if x > 5 and x < 9:
                self.board[x, 3] = square.Floor()
                self.board[x, 4] = square.Floor()

    def viewBoard(self):
        for row in self.board:
            print([str(x) for x in row])

    def runPlayerTurn(self, playerName):
        """Runs the sequence of events for  a player,
        broken up into 3 phases.
        1. Refresh Cards
        2. Equip Items
        3. Take an action
        """
        gameover = False
        print('running ' + playerName + '\'s turn')
        currentPlayer = self.characters[playerName]
        print('Refreshing Cards')
        currentPlayer.refreshCards()
        print('Equipping Items')
        currentPlayer.equipItems()
        print('Taking an action')
        x = query('Choose an action(Run/Battle/Advance/Ready):', ['Run', 'Battle', 'Advance', 'Ready'])
        if x == 'Run':
            options = currentPlayer.checkMovePath(currentPlayer.run(), self.board)
            nums = [str(num) for num in range(len(options))]
            for idx, o in zip(nums, options):
                print(idx + ' ' + str(o))
            choice = query('Choose a square: ', nums)
            currentPlayer.moveToSquare(options[int(choice)][0], options[int(choice)][1], self.board)
        elif x == 'Battle':
            print(playerName + ' is going to attack twice')
        elif x == 'Advance':
            print(playerName + ' is advancing')
            options = currentPlayer.checkMovePath(currentPlayer.speed, self.board)
            nums = [str(num) for num in range(len(options))]
            for idx, o in zip(nums, options):
                print(idx + ' ' + str(o))
            choice = query('Choose a square: ', nums)
            currentPlayer.moveToSquare(options[int(choice)][0], options[int(choice)][1], self.board)
        else:
            print(playerName + ' is readying')
        return gameover

    def runOverloardTurn(self):
        gameover = False
        print('running overlords turn')
        print('Collecting Threat and Drawing Cards')
        curThreat = self.overlord.collectThreat(len(self.characters))
        print('Overlord has ' + str(curThreat) + ' threat.')
        print('Drawing cards')
        print('Spawining Monsters')
        print('Activating Monsters')
        return gameover

    def gameEndMessage(self):
        print('Game over!')

    def start(self):
        print('Starting game!')
        gameover = False
        self.overlord = Overlord('cheese wheel')
        while not gameover:
            #Player Turns starts first and since any player can go first
            #the turn order is determined by choosing a character
            playersRemaining = [name for name in self.characters]
            while playersRemaining:
                self.viewBoard()
                print('Choose a player to use')
                for idx, name in enumerate(playersRemaining):
                    print(str(idx) + ' : ' + name)
                x = query('', [str(num) for num in range(len(playersRemaining))])
                playerName = playersRemaining.pop(int(x))
                gameover = self.runPlayerTurn(playerName)
            #Overloard Player
            gameover = self.runOverloardTurn()
            self.currentRound += 1
        #If gameover, print out some game stats.
        self.gameEndMessage()
