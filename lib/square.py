class Square():
    def __init__(self):
        self.thingsInSquare = []

    def addItemToSquare(self, thing):
        self.thingsInSquare.append(thing)

class Wall(Square):
    def __init__(self):
        super().__init__()

    def __str__(self):
        if self.thingsInSquare:
            return self.thingsInSquare[0].name[0]
        else:
            return ' '

class Floor(Square):
    def __init__(self):
        super().__init__()

    def __str__(self):
        if self.thingsInSquare:
            return self.thingsInSquare[0].name[0]
        else:
            return 'F'