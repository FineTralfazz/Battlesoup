'''
Authors:
    Jacob McKenna
    Chris Bailey
    Brandon Abbott

Created 2/16/18
'''

from board import Board

class Game(object):

	def __init__(self):
		self.boards = [Board(), Board()]

	def get_number_of_boards(self):
		return len(self.boards)
