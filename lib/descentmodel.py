#Imports

class GameBoard():
	def __init__(self, numPlayers):
		self.numPlayers = numPlayers
		self.loadSavedMaps()

	def loadSavedMaps(self):
		print('loading map names into saved dir')

	def loadBoard(self, boardPath):
		print('loading board')