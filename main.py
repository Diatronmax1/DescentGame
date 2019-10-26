#This carries out the management of the game itself.
from lib.charactersheet import CharacterSheet
from lib.character import Character
from lib import descentmodel

def make4FluffCharacters():
    newCharacter0 = Character(CharacterSheet('Bunemaster Thorn',
                                  12,
                                  4,
                                  0,
                                  5,
                                  0,
                                  0,
                                  3,
                                  0,
                                  0,
                                  3,
                                  2,
                                  'base'))
    newCharacter1 = Character(CharacterSheet('Red Scorpion',
                                  12,
                                  4,
                                  1,
                                  4,
                                  1,
                                  1,
                                  1,
                                  1,
                                  1,
                                  1,
                                  3,
                                  'base'))
    newCharacter2 = Character(CharacterSheet('Steelhorns',
                                  16,
                                  3,
                                  1,
                                  4,
                                  3,
                                  0,
                                  0,
                                  3,
                                  0,
                                  0,
                                  3,
                                  'base'))
    newCharacter3 = Character(CharacterSheet('Tonan of the Wild',
                                  12,
                                  4,
                                  1,
                                  5,
                                  1,
                                  2,
                                  0,
                                  1,
                                  2,
                                  0,
                                  3,
                                  'base'))
    return {newCharacter0.name: newCharacter0,
            newCharacter1.name: newCharacter1,
            newCharacter2.name: newCharacter2,
            newCharacter3.name: newCharacter3,}

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

def setup(game):
    game.characters = make4FluffCharacters()
    game.loadBoard('blah')
    #Place chars on squares
    game.characters['Tonan of the Wild'].moveToSquare(0, 0, game.board)
    game.characters['Steelhorns'].moveToSquare(0, 1, game.board)
    game.characters['Red Scorpion'].moveToSquare(1, 0, game.board)
    game.characters['Bunemaster Thorn'].moveToSquare(1, 1, game.board)

if __name__ == '__main__':
    #Query the number of players (1-4)
    #numPlayers = int(query('Enter number of players(1-4): ', ['1', '2', '3', '4']))
    
    newGame = descentmodel.DescentGame(4)
    setup(newGame)
    newGame.start()