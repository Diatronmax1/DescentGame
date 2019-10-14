#Imports
import os, pickle
from . import characterSheet

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
        print('Equipping Items')
        print('Taking an action')
        return gameover

    def runOverloardTurn(self):
        gameover = False
        print('running overlords turn')
        return gameover

    def gameEndMessage(self):
        print('Game over!')

    def start(self):
        print('Starting game!')
        gameover = False
        while not gameover:
            #Player Turns starts first and since any player can go first
            #the turn order is determined by choosing a character
            playersRemaining = [name for name in self.characters]
            while playersRemaining:
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
