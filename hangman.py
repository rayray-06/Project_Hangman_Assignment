## unfinished, stil getting to work 
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
        "message": "",
        "game_over": False
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
    print("ROOM CREATED:", code)  # debug line
    return redirect(url_for("game", room=code))


@app.route("/game")
def game():
    room = request.args.get("room")

    if not room or room not in rooms:
        return redirect(url_for("create"))

    game = rooms[room]

    return render_template(
        "index.html",
        room=room,
        display_word=" ".join(game["display"]),
        wrong_guesses=game["wrong"],
        guessed=game["guessed"],
        current_player=game["current_player"],
        message=game["message"],
        max_wrong=MAX_WRONG,
        game_over=game["game_over"]
    )


@app.route("/guess", methods=["POST"])
def guess():
    room = request.form.get("room")

    if room not in rooms:
        return redirect(url_for("create"))

    game = rooms[room]

    if game["game_over"]:
        return redirect(url_for("game", room=room))

    letter = request.form.get("letter", "").lower().strip()

    if not re.fullmatch(r"[a-z]", letter):
        game["message"] = "Enter a single letter."
        return redirect(url_for("game", room=room))

    if letter in game["guessed"]:
        game["message"] = f"'{letter}' already guessed."
        return redirect(url_for("game", room=room))

    game["guessed"].append(letter)

    correct = False
    if letter in game["word"]:
        correct = True
        for i, c in enumerate(game["word"]):
            if c == letter:
                game["display"][i] = letter
    else:
        game["wrong"] += 1

    if "_" not in game["display"]:
        game["game_over"] = True
        game["message"] = f"Player {game['current_player']} wins!"
    elif game["wrong"] >= MAX_WRONG:
        game["game_over"] = True
        game["message"] = f"Game over. Word was '{game['word']}'."
    elif not correct:
        game["current_player"] = 2 if game["current_player"] == 1 else 1
        game["message"] = f"Wrong! Player {game['current_player']}'s turn."
    else:
        game["message"] = "Correct! Go again."

    return redirect(url_for("game", room=room))


@app.route("/state/<room>")
def state(room):
    if room not in rooms:
        return jsonify({"error": "Room not found"}), 404

    data = rooms[room].copy()
    data["max_wrong"] = MAX_WRONG
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
