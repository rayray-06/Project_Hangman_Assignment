console.log("game.js loaded");

const room = document.body.getAttribute("data-room");
const myPlayer = parseInt(document.body.getAttribute("data-player"), 10);

// Poll server every second for updates
function pollState() {
    fetch(`/state/${room}`)
        .then(res => res.json())
        .then(data => {
            if (!data || data.error) return;

            // Update word
            const wordEl = document.querySelector(".word");
            wordEl.textContent = data.display.join(" ").toUpperCase();

            // Update wrong guesses
            document.querySelector(".info").textContent = `Wrong guesses: ${data.wrong} / ${data.max_wrong}`;

            // Update guessed letters
            const guessedWrap = document.querySelector(".letters");
            guessedWrap.innerHTML = "";
            data.guessed.forEach(l => {
                const pill = document.createElement("div");
                pill.className = "letter-pill";
                pill.textContent = l.toUpperCase();
                guessedWrap.appendChild(pill);
            });

            // Update message
            document.querySelector(".message").textContent = data.message || "";

            // Update turn
            document.querySelector(".turn strong").textContent = data.current_player;

            // Waiting message
            const waitingEl = document.querySelector(".waiting");
            waitingEl.textContent = data.players < 2 ? "Waiting for Player 2 to join..." : "";

            // Show hangman parts
            const parts = document.querySelectorAll(".part");
            parts.forEach((p, index) => {
                if (index < data.wrong) p.classList.add("show");
                else p.classList.remove("show");
            });

            // Input control
            const input = document.querySelector("input[name='letter']");
            const button = document.querySelector("button[type='submit']");
            const disableInput = data.game_over || (data.players >= 2 && data.current_player !== myPlayer) || (data.players < 2 && myPlayer !== 1);
            input.disabled = button.disabled = disableInput;
            if (!disableInput) input.focus();

            // Player labels
            const p1 = document.getElementById("p1");
            const p2 = document.getElementById("p2");
            if (p1 && p2) {
                p1.className = `player${myPlayer===1?" you":""}${data.current_player===1?" active":""}`;
                p2.className = `player${myPlayer===2?" you":""}${data.current_player===2?" active":""}`;
                p2.textContent = data.players < 2 ? "Player 2 (Waiting...)" : "Player 2";
            }
        })
        .catch(err => console.error("Polling error:", err));
}

// Start polling every second
setInterval(pollState, 1000);

// AJAX guess submission to prevent page reload
const form = document.querySelector("form");
form.addEventListener("submit", e => {
    e.preventDefault();
    const input = form.querySelector("input[name='letter']");
    const letter = input.value.trim();
    if (!letter) return;

    fetch("/guess", {
        method: "POST",
        headers: {"Content-Type": "application/x-www-form-urlencoded"},
        body: `room=${room}&letter=${letter}`
    })
    .then(res => res.json())
    .then(data => {
        input.value = "";
        input.focus();
        if (data.error) console.log(data.error);
        // polling will update the rest
    })
    .catch(err => console.error("Guess error:", err));
});
