from boggle import Boggle
from flask import Flask, render_template, request, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
app.debug = True

toolbar = DebugToolbarExtension(app)

boggle_game = Boggle()
@app.route("/", methods=["POST"])
def index():
  session['board'] = []
  board = boggle_game.make_board()
  session['board'].append(board)

  return render_template('index.html', board=board)