console.log("game.js loaded");

// get the room code
const room = document.body.getAttribute("data-room");

// poll the server for updates every second
function pollState() {
    fetch(`/state/${room}`)
        .then(res => res.json())
        .then(data => {

            if (!data || data.error) return;

            // update word display
            const wordEl = document.querySelector(".word");
            wordEl.textContent = data.display.join(" ").toUpperCase();

            // update wrong guesses text
            const wrongEl = document.querySelector(".info");
            wrongEl.textContent = `Wrong guesses: ${data.wrong} / ${data.max_wrong}`;

            // update guessed letters
            const guessedWrap = document.querySelector(".letters");
            guessedWrap.innerHTML = "";
            data.guessed.forEach(l => {
                const pill = document.createElement("div");
                pill.className = "letter-pill";
                pill.textContent = l;
                guessedWrap.appendChild(pill);
            });

            // update message
            document.querySelector(".message").textContent = data.message;

            // update player turn
            document.querySelector(".turn strong").textContent = data.current_player;

            // update hangman parts
            const wrong = data.wrong;
            const parts = document.querySelectorAll(".part");
            parts.forEach((p, index) => {
                if (index < wrong) {
                    p.classList.add("show");
                } else {
                    p.classList.remove("show");
                }
            });
        })
        .catch(err => console.error("polling error:", err));
}

setInterval(pollState, 1000);
