'''
Authors:
    Jacob McKenna
    Chris Bailey
    Brandon Abbott

Created 2/09/18
'''

import unittest
import ship

class Tests(unittest.TestCase):


	ship = ship.Ship(1,1,5)

	def test_ship(self):
		self.assertEqual(1,1)





if __name__ == '__main__':
	unittest.main()