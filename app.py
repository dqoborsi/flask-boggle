from boggle import Boggle
from flask import Flask, render_template, request, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'

boggle_game = Boggle()

@app.route("/")
def homepage():
  board = boggle_game.make_board()
  session['board'] = board
  highscore = session.get('highscore', 0)
  nplays = session.get('nplays', 0)

  return render_template('base.html', board=board, highscore=highscore, nplays=nplays)

@app.route("/check-word")
def check_word():
  word = request.args["word"]
  board = session["board"]
  response = boggle_game.check_valid_word(board, word)

  return jsonify({'result': response})

@app.route("/post-score", methods=["POST"])
def post_score():
  import pdb
  score = request.json["score"]
  pdb.set_trace()
  highscore = session.get("highscore", 0)
  nplays = session.get("nplays", 0)

  session['nplays'] = nplays + 1
  session['highscore'] = max(score, highscore)

  return jsonify(brokeRecord=score > highscore)