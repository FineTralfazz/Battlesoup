'''
Authors:
    Jacob McKenna
    Chris Bailey
    Brandon Abbott

Created 2/09/18
'''

import unittest
from ship import Ship, Directions
from board import Board

class Tests(unittest.TestCase):

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
        ship_N = Ship(1,1,5, Directions.NORTH)
        ship_E = Ship(1,1,5, Directions.EAST)
        ship_S = Ship(1,1,5, Directions.SOUTH)
        ship_W = Ship(1,1,5, Directions.WEST)

        self.assertNotEqual(ship_N.get_pins(), [])
        self.assertEqual(ship_N.get_pins(), [(1,1), (1,2), (1,3), (1,4), (1,5)])

        self.assertNotEqual(ship_E.get_pins(), [])
        self.assertEqual(ship_E.get_pins(), [(1,1), (2,1), (3,1), (4,1), (5,1)])

        self.assertNotEqual(ship_S.get_pins(), [])
        self.assertEqual(ship_S.get_pins(), [(1,1), (1,0), (1,-1), (1,-2), (1,-3)])

        self.assertNotEqual(ship_W.get_pins(), [])
        self.assertEqual(ship_W.get_pins(), [(1,1), (0,1), (-1,1), (-2,1), (-3,1)])

    def test_multiple_different_ship_size_placements(self):
        ship_N = Ship(1,1,2, Directions.NORTH)
        ship_E = Ship(1,1,3, Directions.EAST)
        ship_S = Ship(1,1,4, Directions.SOUTH)
        ship_W = Ship(1,1,5, Directions.WEST)

        self.assertNotEqual(ship_N.get_pins(), [])
        self.assertEqual(ship_N.get_pins(), [(1,1), (1,2)])

        self.assertNotEqual(ship_E.get_pins(), [])
        self.assertEqual(ship_E.get_pins(), [(1,1), (2,1), (3,1)])

        self.assertNotEqual(ship_S.get_pins(), [])
        self.assertEqual(ship_S.get_pins(), [(1,1), (1,0), (1,-1), (1,-2)])

        self.assertNotEqual(ship_W.get_pins(), [])
        self.assertEqual(ship_W.get_pins(), [(1,1), (0,1), (-1,1), (-2,1), (-3,1)])


    def test_multiple_different_ship_placements(self):
        ship_N = Ship(5,5,2, Directions.NORTH)
        ship_E = Ship(3,9,3, Directions.EAST)
        ship_S = Ship(0,9,4, Directions.SOUTH)
        ship_W = Ship(1,5,5, Directions.WEST)

        self.assertNotEqual(ship_N.get_pins(), [])
        self.assertEqual(ship_N.get_pins(), [(5,5), (5,6)])

        self.assertNotEqual(ship_E.get_pins(), [])
        self.assertEqual(ship_E.get_pins(), [(3,9), (4,9), (5,9)])

        self.assertNotEqual(ship_S.get_pins(), [])
        self.assertEqual(ship_S.get_pins(), [(0,9), (0,8), (0,7), (0,6)])

        self.assertNotEqual(ship_W.get_pins(), [])
        self.assertEqual(ship_W.get_pins(), [(1,5), (0,5), (-1,5), (-2,5), (-3,5)])

    def test_board(self):
        board = Board()
        
        board.place_ship(5,5,2, Directions.NORTH)
        board.place_ship(3,9,3, Directions.EAST)
        board.place_ship(0,9,4, Directions.SOUTH)
        # Bad ship placements
        board.place_ship(1,5,5, Directions.WEST)
        board.place_ship(7,7,5, Directions.NORTH)
        board.place_ship(7,7,5, Directions.EAST)
        board.place_ship(1,1,3, Directions.WEST)
        board.place_ship(5,55,2, Directions.NORTH)

        self.assertFalse(board.is_valid_index(-2))
        self.assertFalse(board.is_valid_index(-1))
        self.assertTrue(board.is_valid_index(0))
        self.assertTrue(board.is_valid_index(1))
        self.assertTrue(board.is_valid_index(2))
        self.assertTrue(board.is_valid_index(3))
        self.assertTrue(board.is_valid_index(4))
        self.assertTrue(board.is_valid_index(5))
        self.assertTrue(board.is_valid_index(6))
        self.assertTrue(board.is_valid_index(7))
        self.assertTrue(board.is_valid_index(8))
        self.assertTrue(board.is_valid_index(9))
        self.assertFalse(board.is_valid_index(10))

        self.assertTrue(board.is_valid_placement(1,2,3,Directions.NORTH))
        self.assertTrue(board.is_valid_placement(7,4,1,Directions.NORTH))
        self.assertFalse(board.is_valid_placement(10,4,1,Directions.NORTH))

        
        self.assertEqual(board.get_number_of_ships(), 3)

    def test_bad_board_placement(self):
        board = Board()

        board.place_ship(5,55,2, 10)
        board.place_ship(0,0,111, 10)
        board.place_ship(199,0,0, 10)

        self.assertEqual(board.get_number_of_ships(), 0)
        self.assertEqual(board.get_length(), 9)





if __name__ == '__main__':
    unittest.main()

