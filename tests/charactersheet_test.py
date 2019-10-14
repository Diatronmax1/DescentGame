import sys, unittest

libPath = '../lib/'
if libPath not in sys.path:
	sys.path.insert(0, libPath)

from characterSheet import CharacterSheet

class TestCharacterSheet(unittest.TestCase):

	def test00_makeSheet(self):
		newSheet = CharacterSheet('test')
		self.assertEqual(newSheet.name, 'test')

if __name__ == '__main__':
	unittest.main()