from flask import Flask, render_template_string, request, redirect, session, url_for
from random import choice
import re

app = Flask(__name__)
app.secret_key = "secret-key"

WORD_LIST = ["python", "flask", "hangman", "multiplayer", "development", "programming", "challenge", "session", "template", "function"]
MAX_WRONG = 6

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Multiplayer Hangman</title>
    <style>
        :root{--bg:#f3f4f6;--card:#fff;--accent:#2563EB;--muted:#6b7280}
        body{font-family: Inter, Arial, sans-serif; background:var(--bg); display:flex; min-height:100vh; align-items:center; justify-content:center;}
        .card{width:760px; background:var(--card); border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.08); padding:24px; display:flex; gap:20px}
        .left{width:320px; display:flex; flex-direction:column; align-items:center}
        .right{flex:1}
        h2{margin:0 0 8px 0}
        .svg-wrap{background:#eef2ff; padding:18px; border-radius:8px}
        svg{width:220px; height:300px}
        .word{font-size:34px; letter-spacing:12px; margin-top:18px}
        .turn{margin-top:14px; font-weight:600}
        .info{color:var(--muted); margin-top:6px}
        form{margin-top:16px}
        input[type=text]{font-size:20px; padding:8px 10px; width:80px; text-align:center; border-radius:8px; border:1px solid #e5e7eb}
        button{padding:10px 16px; border-radius:8px; border:0; background:var(--accent); color:white; font-weight:600; cursor:pointer}
        .reset{background:#e5e7eb; color:#111; margin-left:8px}
        .message{margin-top:14px; font-weight:600}
        .guessed{margin-top:10px; color:var(--muted)}
        .letters{display:flex; gap:8px; flex-wrap:wrap; margin-top:8px}
        .letter-pill{padding:6px 10px; background:#f8fafc; border-radius:999px; border:1px solid #eef2ff}
        /* hangman parts hidden by default */
        .part{opacity:0; transition:opacity 300ms ease-in-out;}
        .part.show{opacity:1}
        .small{font-size:14px; color:var(--muted)}
    </style>
</head>
<body>
    <div class="card">
        <div class="left">
            <h2>Multiplayer Hangman</h2>
            <div class="svg-wrap">
                <!-- Gallows + parts. Parts will get class 'show' depending on wrong_guesses -->
                <svg viewBox="0 0 120 160" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                    <!-- gallows -->
                    <line x1="10" y1="150" x2="110" y2="150" stroke="#333" stroke-width="2"/>
                    <line x1="30" y1="150" x2="30" y2="20" stroke="#333" stroke-width="2"/>
                    <line x1="30" y1="20" x2="80" y2="20" stroke="#333" stroke-width="2"/>
                    <line x1="80" y1="20" x2="80" y2="36" stroke="#333" stroke-width="2"/>

                    <!-- head -->
                    <circle cx="80" cy="46" r="10" stroke="#111" stroke-width="2" fill="transparent"
                        class="part {% if wrong_guesses >= 1 %}show{% endif %}" id="head"/>

                    <!-- body -->
                    <line x1="80" y1="56" x2="80" y2="92" stroke="#111" stroke-width="2"
                        class="part {% if wrong_guesses >= 2 %}show{% endif %}" id="body"/>

                    <!-- left arm -->
                    <line x1="80" y1="66" x2="64" y2="80" stroke="#111" stroke-width="2"
                        class="part {% if wrong_guesses >= 3 %}show{% endif %}" id="larm"/>

                    <!-- right arm -->
                    <line x1="80" y1="66" x2="96" y2="80" stroke="#111" stroke-width="2"
                        class="part {% if wrong_guesses >= 4 %}show{% endif %}" id="rarm"/>

                    <!-- left leg -->
                    <line x1="80" y1="92" x2="66" y2="118" stroke="#111" stroke-width="2"
                        class="part {% if wrong_guesses >= 5 %}show{% endif %}" id="lleg"/>

                    <!-- right leg -->
                    <line x1="80" y1="92" x2="94" y2="118" stroke="#111" stroke-width="2"
                        class="part {% if wrong_guesses >= 6 %}show{% endif %}" id="rleg"/>
                </svg>
            </div>

            <div class="small info">Wrong guesses: {{ wrong_guesses }} / {{ max_wrong }}</div>
            <div class="guessed small">Guessed letters:
                <div class="letters">
                    {% for g in guessed %}
                        <div class="letter-pill">{{ g }}</div>
                    {% endfor %}
                </div>
            </div>
        </div>

        <div class="right">
            <div style="display:flex; align-items:center; justify-content:space-between">
                <div>
                    <div class="turn small">Player <strong>{{ current_player }}</strong>'s Turn</div>
                    <div class="word">{{ display_word }}</div>
                </div>
                <div>
                    <form method="POST" action="/reset">
                        <button type="submit" class="reset">New Game</button>
                    </form>
                </div>
            </div>

            <form method="POST" action="/guess">
                <label class="small">Enter a letter</label><br>
                <input name="letter" maxlength="1" autocomplete="off" pattern="[A-Za-z]" {% if game_over %}disabled{% endif %}>
                <button type="submit" {% if game_over %}disabled{% endif %}>Guess</button>
                <div class="message">{{ message }}</div>
            </form>

            <div style="margin-top:18px">
                <div class="small">Rules</div>
                <ol class="small">
                    <li>Players alternate turns. A player continues if their guess is correct.</li>
                    <li>Make a wrong guess to pass the turn to the other player.</li>
                    <li>Max wrong guesses before loss: {{ max_wrong }}.</li>
                </ol>
            </div>
        </div>
    </div>
</body>
</html>
"""


def init_game():
    word = choice(WORD_LIST)
    session["word"] = word
    session["display"] = ["_" for _ in word]
    session["guessed"] = []
    session["wrong"] = 0
    session["current_player"] = 1
    session["message"] = ""
    session["game_over"] = False

@app.route("/")
def index():
    if "word" not in session:
        init_game()

    # Prepare values for template
    message = session.get("message", "")
    display_word = " ".join(session.get("display", []))
    wrong = session.get("wrong", 0)
    guessed = session.get("guessed", [])
    current_player = session.get("current_player", 1)
    game_over = session.get("game_over", False)

    return render_template_string(
        TEMPLATE,
        hangman=None,
        display_word=display_word,
        wrong_guesses=wrong,
        guessed=guessed,
        current_player=current_player,
        message=message,
        max_wrong=MAX_WRONG,
        game_over=game_over
    )

@app.route("/guess", methods=["POST"])
def guess():
    if session.get("game_over", False):
        session["message"] = "Game over — press New Game to play again."
        return redirect(url_for("index"))

    letter = request.form.get("letter", "").lower().strip()

    # validate letter
    if not re.fullmatch(r"[a-z]", letter):
        session["message"] = "Please enter a single letter (A-Z)."
        return redirect(url_for("index"))

    word = session["word"]
    display = session["display"]
    guessed = session["guessed"]

    if letter in guessed:
        session["message"] = f"'{letter}' was already guessed."
        return redirect(url_for("index"))

    # record guess
    guessed.append(letter)

    correct = False
    if letter in word:
        correct = True
        for i, c in enumerate(word):
            if c == letter:
                display[i] = letter

    else:
        session["wrong"] = session.get("wrong", 0) + 1

    # check win
    if "_" not in display:
        session["message"] = f"Player {session['current_player']} wins! The word was '{word}'."
        session["game_over"] = True
        return redirect(url_for("index"))

    # check lose
    if session.get("wrong", 0) >= MAX_WRONG:
        session["message"] = f"No more guesses — players lose. The word was '{word}'."
        session["game_over"] = True
        return redirect(url_for("index"))

    # switch turn only if incorrect
    if not correct:
        session["current_player"] = 2 if session["current_player"] == 1 else 1
        session["message"] = f"Wrong! Turn passes to Player {session['current_player']}."
    else:
        session["message"] = f"Good guess — Player {session['current_player']} goes again."

    return redirect(url_for("index"))

@app.route("/reset", methods=["POST"])
def reset():
    init_game()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
