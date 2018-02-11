'''
Authors:
    Jacob McKenna
    Chris Bailey
    Brandon Abbott

Created 2/10/18
'''

from ship import Ship

class Board(object):

	def __init__(self):
		self.board = []

	def place_ship(self, x, y, l, d):
		self.board.append(Ship(x, y, l, d))

	def get_number_of_ships(self):
		return len(self.board)