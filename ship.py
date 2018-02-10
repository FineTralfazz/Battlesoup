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

    def get_x(self):
       return self.x

    def get_y(self):
       return self.y

    def get_length(self):
        return self.length

    def get_direction(self):
        return self.direction

    # def create_pin_spaces(self):
    #     for ll in self.length:
