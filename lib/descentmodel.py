#Imports
import os
from . import character

class DescentGame():
    def __init__(self, numPlayers):
        self.numPlayers = numPlayers
        self.characterDir = os.path.join(os.path.dirname(__file__), 'characters/')
        self.mapDir = os.path.join(os.path.dirname(__file__), 'maps/')
        self.loadSavedMaps(self.mapDir)
        self.loadSavedCharacters(self.characterDir)

    def loadSavedMaps(self, mapDir):
        print('Loading available maps from ' + mapDir)

    def loadSavedCharacters(self, charDir):
        print('loading characters from ' + charDir)

    def createCharacter(self, charName):


    def loadBoard(self, boardPath):
        print('loading board')