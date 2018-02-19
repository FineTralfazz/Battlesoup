'''
Authors:
    Jacob McKenna
    Chris Bailey
    Brandon Abbott

Created 2/09/18
'''
from enum import Enum

class Directions(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Ship(object):

    def __init__(self, x, y, length, direction):
       self.x = x
       self.y = y
       self.length = length
       self.direction = direction
       self.pins = [(self.x,self.y)]
       self.set_pin_spaces()

    def get_x(self):
       return self.x

    def get_y(self):
       return self.y

    def get_length(self):
        return self.length

    def get_direction(self):
        return self.direction

    def get_pins(self):
        return self.pins

    def append_pin_tuple(self, x, y):
        self.pins.append((x, y))

    def set_pin_spaces(self):
        x, y = self.x, self.y

        for ll in range(self.length - 1):
            if self.direction == Directions.NORTH:
                y = y - 1
            elif self.direction == Directions.EAST:
                x = x - 1
            elif self.direction == Directions.SOUTH:
                y = y + 1
            elif self.direction == Directions.WEST:
                x = x + 1

            self.append_pin_tuple(x,y)

        print('Pins at:')
        print(self.pins)