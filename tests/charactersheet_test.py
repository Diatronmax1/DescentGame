import sys, unittest

libPath = '../lib/'
if libPath not in sys.path:
	sys.path.insert(0, libPath)

from characterSheet import CharacterSheet

class TestCharacterSheet(unittest.TestCase):

	def test00_makeSheet(self):
		newSheet = CharacterSheet('test')
		self.assertEqual(newSheet.name, 'test')

	def test01_setHealthParam(self):
		newSheet = CharacterSheet('test')
		newSheet.setParam('health', 1)
		self.assertEqual(newSheet.health, 1)

	def test02_setHealthParamString(self):
		newSheet = CharacterSheet('test')
		newSheet.setParam('health', '1')
		self.assertEqual(newSheet.health, 1)

	def test03_setHealthParamFloat(self):
		newSheet = CharacterSheet('test')
		newSheet.setParam('health', 1.2)
		self.assertEqual(newSheet.health, 1)

	def test04_setHealthParamStrFloat(self):
		newSheet = CharacterSheet('test')
		newSheet.setParam('health', '1.8')
		self.assertEqual(newSheet.health, 2)

	def test05_setParamDoesntExist(self):
		newSheet = CharacterSheet('test')
		msg = newSheet.setParam('watermelon', '2')
		self.assertEqual(msg, 'watermelon not in Character Sheet, cant modify')

	def test06_setParamNegativeValue(self):
		newSheet = CharacterSheet('test')
		msg = newSheet.setParam('health', -2)
		self.assertEqual(msg, 'Value -2 cannot be < 0')
		self.assertEqual(newSheet.health, 0)

	def test07_setParamNegativeStrValue(self):
		newSheet = CharacterSheet('test')
		msg = newSheet.setParam('fatigue', '-2')
		self.assertEqual(msg, 'Value: -2.0 must be >= 0')

	def test08_setParamInvalidString(self):
		newSheet = CharacterSheet('test')
		msg = newSheet.setParam('fatigue', 'cheese')
		self.assertEqual(msg, 'Cant convert cheese to int >= 0')

if __name__ == '__main__':
	unittest.main()