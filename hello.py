'''
Authors:
    Jacob McKenna
    Chris Bailey
    Brandon Abbott

Created 2/09/18
'''

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Battleship!"