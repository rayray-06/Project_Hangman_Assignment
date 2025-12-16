from flask import Flask, render_template, request, redirect, url_for, jsonify
from random import choice
import string
import re

app = Flask(__name__)
app.secret_key = "secret-key"

WORD_LIST = [
    "python", "flask", "hangman", "multiplayer",
    "development", "programming", "challenge",
    "session", "template", "function"
]

MAX_WRONG = 6
rooms = {}


def create_room():
    code = ''.join(choice(string.ascii_uppercase) for _ in range(5))
    word = choice(WORD_LIST)

    rooms[code] = {
    "word": word,
    "display": ["_" for _ in word],
    "guessed": [],
    "wrong": 0,
    "current_player": 1,
    "message": "Waiting for Player 2 to join...",
    "game_over": False,
    "players": 1
}


    return code


@app.route("/")
def home():
    return render_template("homepage.html")


@app.route("/create")
def create():
    return render_template("create_join.html")



@app.route("/create_room", methods=["POST"])
def create_room_route():
    code = create_room()
    return redirect(url_for("game", room=code, player=1))


@app.route("/join_room", methods=["POST"])
def join_room():
    room = request.form.get("room", "").upper()

    if room not in rooms:
        return redirect(url_for("create"))

    if rooms[room]["players"] < 2:
        rooms[room]["players"] = 2
        rooms[room]["message"] = "Player 2 joined! Player 1 starts."

    return redirect(url_for("game", room=room, player=2))



@app.route("/game")
def game():
    room = request.args.get("room")
    player = int(request.args.get("player", 1))

    if not room or room not in rooms:
        return redirect(url_for("create"))

    game = rooms[room]

    return render_template(
        "index.html",
        room=room,
        player=player,
        display_word=" ".join(game["display"]),
        wrong_guesses=game["wrong"],
        guessed=game["guessed"],
        current_player=game["current_player"],
        message=game["message"],
        max_wrong=MAX_WRONG,
        game_over=game["game_over"],
        players=game["players"]
    )


@app.route("/guess", methods=["POST"])
def guess():
    room = request.form.get("room")
    if room not in rooms:
        return jsonify({"error": "Room not found"}), 404

    game = rooms[room]
    if game["game_over"]:
        return jsonify({"error": "Game over"}), 400

    letter = request.form.get("letter", "").lower().strip()
    if not re.fullmatch(r"[a-z]", letter):
        game["message"] = "Enter a single letter."
        return jsonify({"error": "Invalid letter"}), 400

    if letter in game["guessed"]:
        game["message"] = f"'{letter}' already guessed."
        return jsonify({"error": "Already guessed"}), 400

    game["guessed"].append(letter)
    correct = False
    if letter in game["word"]:
        correct = True
        for i, c in enumerate(game["word"]):
            if c == letter:
                game["display"][i] = letter
    else:
        game["wrong"] += 1

    # Determine if game is over
    if "_" not in game["display"]:
        game["game_over"] = True
        game["message"] = f"Player {game['current_player']} wins!"
    elif game["wrong"] >= MAX_WRONG:
        game["game_over"] = True
        game["message"] = f"Game over. Word was '{game['word']}'."
    elif not correct:
        # Switch turn only if wrong
        game["current_player"] = 2 if game["current_player"] == 1 else 1
        game["message"] = f"Wrong! Player {game['current_player']}'s turn."
    else:
        game["message"] = "Correct! Go again."

    # Return updated game state
    return jsonify({
        "display": game["display"],
        "wrong": game["wrong"],
        "guessed": game["guessed"],
        "current_player": game["current_player"],
        "message": game["message"],
        "game_over": game["game_over"],
        "players": game["players"],
        "max_wrong": MAX_WRONG
    })


@app.route("/state/<room>")
def state(room):
    if room not in rooms:
        return jsonify({"error": "Room not found"}), 404

    game = rooms[room]
    return jsonify({
        "display": game["display"],
        "wrong": game["wrong"],
        "guessed": game["guessed"],
        "current_player": game["current_player"],
        "message": game["message"],
        "game_over": game["game_over"],
        "players": game["players"],
        "max_wrong": MAX_WRONG
    })




if __name__ == "__main__":
    app.run(debug=True)
