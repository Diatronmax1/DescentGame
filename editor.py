from lib import descentmodel
from lib.characterSheet import CharacterSheet

def queryStr(queryMsg, acceptedMsgs = []):
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

def queryNum(queryMsg, lowlim=None, highlim=None):
    """Retrieves a number inside lowlim inclusive, highlim exclusive
    """
    passLow = True
    passHigh = True
    while True:
        x = input(queryMsg)
        try:
            val = round(float(x))
            if lowlim is not None:
                if val < lowlim:
                    passLow = False
                    print(x + ' not greater than ' + str(lowlim))
                else:
                    passLow = True
            if highlim is not None:
                if val >= highlim:
                    passHigh = False
                    print(x + ' not less than ' + str(highlim))
                else:
                    passHigh = True
            if passLow and passHigh:
                return val
        except:
            print(x + 'not a numeric value')

def createCharacter():

    name = queryStr('Character Name: ')
    health = queryNum('Health: ', 0)
    fatigue = queryNum('Fatigue: ', 0)
    armor = queryNum('Armor: ', 0)
    speed = queryNum('Speed: ', 0)
    meleeTrait = queryNum('Melee Trait: ', 0)
    rangeTrait = queryNum('Range Trait: ', 0)
    magicTrait = queryNum('Magic Trait: ', 0)
    fightingSkill = queryNum('Fighting Skill: ', 0)
    subterfugeSkill = queryNum('Subterfuge Skill: ', 0)
    wizardrySkill = queryNum('Wizardy Skill: ', 0)
    conquestValue = queryNum('Conquest Value: ', 0)
    expansion = queryStr('Expansion: ', ['base'])
    return CharacterSheet(name, 
                          health, 
                          fatigue, 
                          armor, 
                          speed, 
                          meleeTrait, 
                          rangeTrait, 
                          magicTrait, 
                          fightingSkill, 
                          subterfugeSkill, 
                          wizardrySkill, 
                          conquestValue, 
                          expansion)

def saveCharacter(characterDir, character):
    print('Saving ' + character.name + ' in ' + characterDir)
    
if __name__ == '__main__':
    newModel = descentmodel.DescentGame(4)
    newCharacter = createCharacter()
    # newCharacter = CharacterSheet('Runemaster Thorn',
    #                               12,
    #                               4,
    #                               0,
    #                               5,
    #                               0,
    #                               0,
    #                               3,
    #                               0,
    #                               0,
    #                               3,
    #                               2,
    #                               'base')
    print(newCharacter)
    saveCharacter(newModel.characterDir, newCharacter)