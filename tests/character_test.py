import sys, unittest

libPath = '../lib/'
if libPath not in sys.path:
    sys.path.insert(0, libPath)

from charactersheet import CharacterSheet
from character import Character

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
        newChar = Character(self.magicChar)
        self.assertEqual(newChar.health, 12)
        self.assertEqual(newChar.fatigue, 4)
        self.assertEqual(newChar.armor, 0)
        self.assertEqual(newChar.speed, 5)
        self.assertEqual(newChar.money, 0)

    def test01_takeSomeDamage(self):
        newChar = Character(self.magicChar)
        newChar.takeDamage(3)
        self.assertEqual(newChar.health, 9)

    def test02_takeDamageWithArmor(self):
        newChar = Character(self.meleeChar)
        newChar.takeDamage(3)
        self.assertEqual(newChar.health, 14)

    def test03_pingDamageintoArmor(self):
        newChar = Character(self.meleeChar)
        newChar.takeDamage(1)
        self.assertEqual(newChar.health, 16)

    def test04_die(self):
        newChar = Character(self.magicChar)
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
        newChar = Character(self.magicChar)
        conquest = newChar.takeDamage(12)
        self.assertEqual(conquest, 2)
        self.assertEqual(newChar.health, 12)
        self.assertEqual(newChar.fatigue, 4)
        self.assertEqual(newChar.money, 0)
        self.assertEqual(newChar.mapLocation, 'town')

if __name__ == '__main__':
    unittest.main()