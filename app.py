from boggle import Boggle
from flask import Flask, render_template, request, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.debug = True

toolbar = DebugToolbarExtension(app)

boggle_game = Boggle()
@app.route("/")
def index():
  board = boggle_game.make_board()
  session['board'] = board

  return render_template('index.html', board=board)