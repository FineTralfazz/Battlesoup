'''
Authors:
    Jacob McKenna
    Chris Bailey
    Brandon Abbott

Created 2/10/18
'''

from ship import Ship, Directions

class Board(object):

    def __init__(self):
        self.board = []
        self.length = 9

    def get_length(self):
        return self.length

    def is_valid_direction(self, direction):
        if direction not in Directions:
            return False
        return True

    def is_valid_index(self,val):
        if (val < 0 or val > self.length):
            return False
        return True

    def is_ship_placed_on_ship(self, poss_ship):

        for ship in self.board:
            for pin in poss_ship.get_pins():
                if pin in ship.get_pins():
                    return False
        return True

    def is_ship_out_of_bounds(self, ship):
        for coord in ship.get_pins():
            if not self.is_valid_index(coord[0]):
                return False
            if not self.is_valid_index(coord[1]):
                return False                
            
        return True

    def is_valid_placement(self, x, y, l, d):
        if not self.is_valid_index(l):
            return False
        if not self.is_valid_direction(d):
            return False 

        ship = Ship(x,y,l,d)
        if not self.is_ship_out_of_bounds(ship):
            return False       
        if not self.is_ship_placed_on_ship(ship):
            return False

        return True

    def place_ship(self, x, y, l, d):
        if not self.is_valid_placement(x,y,l,d):
            return

        self.board.append(Ship(x, y, l, d))

    def get_number_of_ships(self):
        return len(self.board)

