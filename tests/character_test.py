import sys, unittest, numpy as np

libPath = '../lib/'
if libPath not in sys.path:
    sys.path.insert(0, libPath)

from charactersheet import CharacterSheet
import character
import square

class TestCharacterSheet(unittest.TestCase):

    def setUp(self):
        #Make a character Sheet
        self.meleeChar = CharacterSheet('Steelhorns',
                                        health=16,
                                        fatigue=3,
                                        armor=1,
                                        speed=4,
                                        meleeTrait=3,
                                        rangeTrait=0,
                                        magicTrait=0,
                                        fightingSkill=3,
                                        subterfugeSkill=0,
                                        wizardrySkill=0,
                                        conquestValue=3,
                                        expansion='base')
        self.magicChar = CharacterSheet('Runemaster Thorn',
                                        health=12,
                                        fatigue=4,
                                        armor=0,
                                        speed=5,
                                        meleeTrait=0,
                                        rangeTrait=0,
                                        magicTrait=3,
                                        fightingSkill=0,
                                        subterfugeSkill=0,
                                        wizardrySkill=3,
                                        conquestValue=2,
                                        expansion='base')

    def test00_makeCharacter(self):
        newChar = character.Character(self.magicChar)
        self.assertEqual(newChar.health, 12)
        self.assertEqual(newChar.fatigue, 4)
        self.assertEqual(newChar.armor, 0)
        self.assertEqual(newChar.speed, 5)
        self.assertEqual(newChar.money, 0)

    def test01_takeSomeDamage(self):
        newChar = character.Character(self.magicChar)
        newChar.takeDamage(3)
        self.assertEqual(newChar.health, 9)

    def test02_takeDamageWithArmor(self):
        newChar = character.Character(self.meleeChar)
        newChar.takeDamage(3)
        self.assertEqual(newChar.health, 14)

    def test03_pingDamageintoArmor(self):
        newChar = character.Character(self.meleeChar)
        newChar.takeDamage(1)
        self.assertEqual(newChar.health, 16)

    def test04_die(self):
        newChar = character.Character(self.magicChar)
        newChar.health = 4
        newChar.fatigue = 1
        newChar.money = 125
        newChar.mapLocation = 'dungeon'
        newChar.die()
        self.assertEqual(newChar.health, 12)
        self.assertEqual(newChar.fatigue, 4)
        self.assertEqual(newChar.money, 75)
        self.assertEqual(newChar.mapLocation, 'town')

    def test05_takeEnoughDamageToKill(self):
        newChar = character.Character(self.magicChar)
        conquest = newChar.takeDamage(12)
        self.assertEqual(conquest, 2)
        self.assertEqual(newChar.health, 12)
        self.assertEqual(newChar.fatigue, 4)
        self.assertEqual(newChar.money, 0)
        self.assertEqual(newChar.mapLocation, 'town')

    def test06_makeNode(self):
        newNode = character.Node(0, 0, True)
        self.assertEqual(newNode.x, 0)
        self.assertEqual(newNode.y, 0)
        self.assertTrue(newNode.walkable)
        self.assertEqual(newNode.gcost, 0)
        self.assertEqual(newNode.hcost, 0)
        self.assertIsNone(newNode.parent)

    def test07_calculateHCost(self):
        newNode = character.Node(0, 0, True)
        targetNode = character.Node(5, 0, True)
        newNode.calculateHCost(targetNode)
        self.assertEqual(newNode.hcost, 5)

    def test08_calculateHCostDiagonal(self):
        newNode = character.Node(0, 0, True)
        targetNode = character.Node(5, 5, True)
        newNode.calculateHCost(targetNode)
        self.assertEqual(newNode.hcost, 5)

    def test09_calculateHCostReverseDiagonal(self):
        newNode = character.Node(5, 5, True)
        targetNode = character.Node(0, 0, True)
        newNode.calculateHCost(targetNode)
        self.assertEqual(newNode.hcost, 5)

    def test10RetracePath(self):
        endNode =   character.Node(3, 3, True)
        oneBack =   character.Node(2, 3, True)
        twoBack =   character.Node(1, 3, True)
        threeBack = character.Node(0, 3, True)
        endNode.parent = oneBack
        oneBack.parent = twoBack
        twoBack.parent = threeBack
        path = character.retracePath(endNode)
        expectedPath = [(1, 3), (2, 3), (3, 3)]
        for rPath, ePath in zip(path, expectedPath):
            self.assertEqual(rPath, ePath)

    def test11PathTestPtp(self):
        board = np.empty((20, 20), dtype=object)
        for x in range(20):
            for y in range(20):
                newSquare = square.Wall()
                board[x,y] = newSquare
        board[0, 0] = square.Floor()
        board[0, 1] = square.Floor()
        board[0, 2] = square.Floor()
        startX = 0
        startY = 0
        target = (0, 2)
        movespeed = 3
        path = character.pathfind(startX, startY, target, board, movespeed)
        ePath = [(0, 1), (0, 2)]
        for p, eP in zip(path, ePath):
            self.assertEqual(p, eP)

    def test12PathTestWithObstruction(self):
        board = np.empty((20, 20), dtype=object)
        for x in range(20):
            for y in range(20):
                newSquare = square.Wall()
                board[x,y] = newSquare
        board[0, 0] = square.Floor()
        board[0, 1] = square.Floor()
        board[0, 2] = square.Floor()
        #Wall
        #board[0, 3] = square.Floor()
        board[0, 4] = square.Floor()
        board[0, 5] = square.Floor()
        board[1, 0] = square.Floor()
        board[1, 1] = square.Floor()
        #Wall
        #board[1, 2] = square.Floor()
        board[1, 3] = square.Floor()
        board[1, 4] = square.Floor()
        board[1, 5] = square.Floor()
        startX = 0
        startY = 0
        target = (1, 5)
        movespeed = 3
        path = character.pathfind(startX, startY, target, board, movespeed)
        print(path)
        ePath = [(0, 1), (0, 2), (1, 3), (1, 4), (1, 5)]
        for p, eP in zip(path, ePath):
            self.assertEqual(p, eP)

    def test12GetRing(self):
        board = np.empty((20, 20), dtype=object)
        for x in range(20):
            for y in range(20):
                newSquare = square.Wall()
                board[x,y] = newSquare
        board[0, 0] = square.Floor()
        board[0, 1] = square.Floor()
        board[0, 2] = square.Floor()
        targets = character.getRing(0, 0, 1, board)
        eTargets = [(0, 1), (1, 0), (1, 1)]
        for t, eT in zip(targets, eTargets):
            self.assertEqual(t, eT)

if __name__ == '__main__':
    unittest.main()