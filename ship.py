'''
Authors:
    Jacob McKenna
    Chris Bailey
    Brandon Abbott

Created 2/09/18
'''

class Ship(object):

    def __init__(self, x, y, length):
       self.x = x
       self.y = y
       self.length = length

    def get_x(self):
       return self.x

    def get_y(self):
       return self.y

    def get_length(self):
        return self.length