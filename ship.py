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
       self.create_pin_spaces()

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

    def create_pin_spaces(self):
        for ll in range(self.length - 1):
            if self.direction == Directions.NORTH:
                self.y = self.y + 1
                self.pins.append( (self.x, self.y) )













