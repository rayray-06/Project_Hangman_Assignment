console.log("game.js loaded");

const room = document.body.getAttribute("data-room");

function pollState() {
    fetch(`/state/${room}`)
        .then(res => res.json())
        .then(data => {
            if (!data || data.error) return;

            document.querySelector(".word").textContent =
                data.display.join(" ").toUpperCase();

            document.querySelector(".info").textContent =
                `Wrong guesses: ${data.wrong} / ${data.max_wrong}`;

            const guessedWrap = document.querySelector(".letters");
            guessedWrap.innerHTML = "";
            data.guessed.forEach(l => {
                const pill = document.createElement("div");
                pill.className = "letter-pill";
                pill.textContent = l;
                guessedWrap.appendChild(pill);
            });

            document.querySelector(".message").textContent = data.message;
            document.querySelector(".turn strong").textContent = data.current_player;

            const parts = document.querySelectorAll(".part");
            parts.forEach((p, i) => {
                p.classList.toggle("show", i < data.wrong);
            });
        });
}

setInterval(pollState, 1000);


