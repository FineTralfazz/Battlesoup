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
        'phase': 'setup',
        'player1_board': Board(),
        'player2_board': Board(),
        'player1_status': 'setup',
        'player2_status': 'setup',
        'player1_guesses': [],
        'player2_guesses': []
    }
    return jsonify({'success': True})

def switch_turn ():
    global game
    if game['turn'] == 1:
        game['turn'] = 2
    else:
        game['turn'] = 1

def get_board_for_player(player):
    global game
    if int(player) == 1:
        return game['player1_board']
    else:
        return game['player2_board']

def set_board_for_player(player, board):
    global game
    if int(player) == 1:
        game['player1_board'] = board
    else:
        game['player2_board'] = board

def get_guesses_for_player(player):
    global game
    if int(player) == 1:
        return game['player1_guesses']
    else:
        return game['player2_guesses']

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

def get_opponent(player):
    if int(player) == 1:
        return 2
    else:
        return 1

@app.route('/place')
def place():
    global game
    board = get_board_for_player(request.args.get('player'))
    success = board.place_ship(int(request.args.get('x')),
        int(request.args.get('y')),
        int(request.args.get('length')),
        direction_from_int(int(request.args.get('direction'))))
    if len(board.board) == 4:
        game['player' + request.args.get('player') + '_status'] = 'ready'
        if game['player1_status'] == 'ready' and game['player2_status'] == 'ready':
            game['phase'] = 'play'
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

@app.route('/game_status')
def game_status():
    status = {
        'turn': game['turn'],
        'phase': game['phase'],
        'player1_status': game['player1_status'],
        'player2_status': game['player2_status']
    }
    return jsonify(status)

@app.route('/guess')
def guess():
    global game
    player = int(request.args.get('player'))
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    opponent = get_opponent(player)
    opponent_board = get_board_for_player(opponent)
    guesses = get_guesses_for_player(player)
    if player == game['turn']:
        for pin in opponent_board.get_pins():
            if pin['x'] == x and pin['y'] == y:
                guesses.append({'x': x, 'y': y, 'hit': True, 'length': pin['length']})
                switch_turn()
                return jsonify({'hit': True})
        guesses.append({'x': x, 'y': y, 'hit': False, 'length': 0})
        switch_turn()
        return jsonify({'hit': False})
    else:
        return jsonify({'success':False})

@app.route('/guesses')
def guesses():
    player = request.args.get('player')
    guesses = get_guesses_for_player(player)
    return jsonify({'guesses': guesses})
