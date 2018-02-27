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
        else:
            return True

    def is_valid_index(self,val):
        if (val < 0 or val > self.length):
            return False
        return True

    def is_ship_colliding(self, poss_ship):
        for ship in self.board:
            for ii, pin in enumerate(poss_ship.get_pins()):
                if pin in ship.get_pins():
                    # print(pin, 'is in' ship.get_pins())
                    return True
        return False

    def is_ship_out_of_bounds(self, ship):
        for coord in ship.get_pins():
            if not self.is_valid_index(coord[0]):
                return True
            if not self.is_valid_index(coord[1]):
                return True                
            
        return False

    def is_valid_placement(self, x, y, l, d):
        if not self.is_valid_index(l):
            print('Invalid length')
            return False
        if not self.is_valid_direction(d):
            print('invalid direction')
            return False 

        ship = Ship(x,y,l,d)
        if self.is_ship_out_of_bounds(ship):
            print('out of bounds')
            return False       
        if self.is_ship_colliding(ship):
            print('collision')
            return False

        return True

    def place_ship(self, x, y, l, d):
        if not self.is_valid_placement(x,y,l,d):
            return False
        self.board.append(Ship(x, y, l, d))
        return True

    def get_number_of_ships(self):
        return len(self.board)

    def get_pins(self):
        result = []
        for ship in self.board:
            for pin in ship.get_pins():
                result.append({'x': pin[0], 'y': pin[1], 'length': ship.get_length()})
        return result