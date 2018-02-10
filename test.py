'''
Authors:
    Jacob McKenna
    Chris Bailey
    Brandon Abbott

Created 2/09/18
'''

import unittest
from ship import Ship, Directions

class Tests(unittest.TestCase):

    ship = Ship(1,1,5, Directions.NORTH)

    ###############################
    ######## Test Suites ##########
    ###############################

    def test_ship_placement(self):
       self.assertEqual(self.ship.get_x(),1)
       self.assertEqual(self.ship.get_y(),1)
       self.assertEqual(self.ship.get_length(),5)
       self.assertEqual(self.ship.get_direction(), Directions.NORTH)

    def test_ship_pins(self):
        self.assertNotEqual(self.ship.get_pins(), [])
        self.assertEqual(self.ship.get_pins(), [(1,1)])




if __name__ == '__main__':
    unittest.main()

