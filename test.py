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

    def test_single_ship_placement(self):
        ship = Ship(1,1,5, Directions.NORTH)
        self.assertEqual(ship.get_x(),1)
        self.assertEqual(ship.get_y(),1)
        self.assertEqual(ship.get_length(),5)
        self.assertEqual(ship.get_direction(), Directions.NORTH)

    def test_multiple_ship_placements(self):
        shipN = Ship(1,1,5, Directions.NORTH)
        shipE = Ship(1,1,5, Directions.EAST)
        shipS = Ship(1,1,5, Directions.SOUTH)
        shipW = Ship(1,1,5, Directions.WEST)

        self.assertNotEqual(shipN.get_pins(), [])
        self.assertEqual(shipN.get_pins(), [(1,1), (1,2), (1,3), (1,4), (1,5)])

        self.assertNotEqual(shipE.get_pins(), [])
        self.assertEqual(shipE.get_pins(), [(1,1), (2,1), (3,1), (4,1), (5,1)])

        self.assertNotEqual(shipS.get_pins(), [])
        self.assertEqual(shipS.get_pins(), [(1,1), (1,0), (1,-1), (1,-2), (1,-3)])

        self.assertNotEqual(shipW.get_pins(), [])
        self.assertEqual(shipW.get_pins(), [(1,1), (0,1), (-1,1), (-2,1), (-3,1)])

    def test_multiple_different_ship_size_placements(self):
        shipN = Ship(1,1,2, Directions.NORTH)
        shipE = Ship(1,1,3, Directions.EAST)
        shipS = Ship(1,1,4, Directions.SOUTH)
        shipW = Ship(1,1,5, Directions.WEST)

        self.assertNotEqual(shipN.get_pins(), [])
        self.assertEqual(shipN.get_pins(), [(1,1), (1,2)])

        self.assertNotEqual(shipE.get_pins(), [])
        self.assertEqual(shipE.get_pins(), [(1,1), (2,1), (3,1)])

        self.assertNotEqual(shipS.get_pins(), [])
        self.assertEqual(shipS.get_pins(), [(1,1), (1,0), (1,-1), (1,-2)])

        self.assertNotEqual(shipW.get_pins(), [])
        self.assertEqual(shipW.get_pins(), [(1,1), (0,1), (-1,1), (-2,1), (-3,1)])


    def test_multiple_different_ship_placements(self):
        shipN = Ship(5,5,2, Directions.NORTH)
        shipE = Ship(3,9,3, Directions.EAST)
        shipS = Ship(0,9,4, Directions.SOUTH)
        shipW = Ship(1,5,5, Directions.WEST)

        self.assertNotEqual(shipN.get_pins(), [])
        self.assertEqual(shipN.get_pins(), [(5,5), (5,6)])

        self.assertNotEqual(shipE.get_pins(), [])
        self.assertEqual(shipE.get_pins(), [(3,9), (4,9), (5,9)])

        self.assertNotEqual(shipS.get_pins(), [])
        self.assertEqual(shipS.get_pins(), [(0,9), (0,8), (0,7), (0,6)])

        self.assertNotEqual(shipW.get_pins(), [])
        self.assertEqual(shipW.get_pins(), [(1,5), (0,5), (-1,5), (-2,5), (-3,5)])






if __name__ == '__main__':
    unittest.main()

