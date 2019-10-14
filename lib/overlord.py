class Overlord():
    def __init__(self, name):
        self.name = name
        self.threat = 0
        self.cards = 0
        self.powers = {}

    def collectThreat(self, numPlayers):
        self.threat += numPlayers
        return self.threat

    def drawCards(self):
        pass
