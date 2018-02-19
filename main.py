'''
Authors:
    Jacob McKenna
    Chris Bailey
    Brandon Abbott

Created 2/09/18
'''

from flask import Flask, jsonify, render_template, request, g
from ship import Ship, Directions
from board import Board
app = Flask(__name__)
game = {}

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/start_game')
def start_game():
    global game # This is gross, but easier than using a real database
    game = {
        'turn': 1,
        'player1_board': Board(),
        'player2_board': Board()
    }
    return jsonify({'success': True})

def get_board_for_player(player):
    global game
    if player == 1:
        return game['player1_board']
    else:
        return game['player2_board']

def set_board_for_player(player, board):
    global game
    if int(player) == 1:
        game['player1_board'] = board
    else:
        game['player2_board'] = board

def direction_from_int(int_direction):
    if int_direction == 0:
        return Directions.NORTH
    elif int_direction == 1:
        return Directions.EAST
    elif int_direction == 2:
        return Directions.SOUTH
    elif int_direction == 3:
        return Directions.WEST
    else:
        raise

@app.route('/place')
def place():
    board = get_board_for_player(request.args.get('player'))
    success = board.place_ship(int(request.args.get('x')), 
        int(request.args.get('y')),
        int(request.args.get('length')),
        direction_from_int(int(request.args.get('direction'))))
    return jsonify({'success': success})

@app.route('/board')
def get_board():
    board = get_board_for_player(request.args.get('player'))
    result = {
        'ships':[]
    }
    for ship in board.board:
        ship_dict = {'pins': []}
        for pin in ship.get_pins():
            ship_dict['pins'].append([pin[0], pin[1]])
        result['ships'].append(ship_dict)
    return jsonify(result)


