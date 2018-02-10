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

    ###############################
    ######## Test Suites ##########
    ###############################

    def test_ship_xy_length_values(self):
       self.assertEqual(self.ship.get_x(),1)
       self.assertEqual(self.ship.get_y(),1)
       self.assertEqual(self.ship.get_length(),5)





if __name__ == '__main__':
    unittest.main()

