



lyric_list = (info.song_lyrics);
let count = 1

const correctArtist = info.song_artist;
const correctSongName = info.song_name;

const lyricField = document.getElementById("lyric-field");

const moreButton = document.getElementById("more");
const checkButton = document.getElementById("check");

const songInput = document.getElementById("song-input");


const artistInput = document.getElementById("artist-input");

let reachedEnd = false;

addLyrics();

moreButton.addEventListener("click", function () {
    if (count >= (lyric_list).length && !reachedEnd) {
        let givenLyric = document.createElement("div");
        givenLyric.textContent = "END OF LYRICS";
        lyricField.appendChild(givenLyric);
        reachedEnd = true;

    }
    else {

        addLyrics();

    }

})

function addLyrics() {
    for (let j = 0; j < 10; j++) {
        if (count >= lyric_list.length) {
            break;
        }

        let givenLyric = document.createElement("p");
        givenLyric.textContent = lyric_list[count];
        lyricField.appendChild(givenLyric);
        count += 1;
    }
}

let numWrong = 0;

checkButton.addEventListener("click", function () {
    bothCorrect = true
    console.log(songInput.value);
    if (songInput.value.toLowerCase() != correctSongName.toLowerCase()) {
        bothCorrect = false;
    }

    if (artistInput.value.toLowerCase() != correctArtist.toLowerCase()) {
        bothCorrect = false;


    }

    if (bothCorrect == true) {
        let correct = document.createElement("div");
        correct.style.color = 'green';
        correct.style.fontSize = '40px';
        correct.textContent = "CORRECT";

        document.querySelector(".container .input-fields .correct-incorrect").classList.remove("incorrect");
        document.querySelector(".container .input-fields .correct-incorrect").textContent = "CORRECT";
        document.querySelector(".container .input-fields .correct-incorrect").classList.add("correct");
    }
    else {
        if (numWrong < 3) {
            document.querySelector(".container .input-fields .correct-incorrect").textContent += " X"

            document.querySelector(".container .input-fields .correct-incorrect").classList.add("incorrect");
            numWrong += 1;
        }
    }

    if (numWrong == 3) {
        document.getElementById("lyric-field").style.display = "none";

        answer1 = document.createElement("div")
        answer1.classList = "answer";

        answer2 = document.createElement("div");
        answer2.classList = "answer"

        answer1.textContent = correctArtist;
        answer2.textContent = correctSongName;

        document.querySelector(".container").appendChild(answer1);
        document.querySelector(".container").appendChild(answer2);

        buttonField = document.querySelector(".container .button-field")

        while (buttonField.firstChild) {
            buttonField.removeChild(buttonField.firstChild);
        }

        reset = document.createElement("button");
        reset.textContent = "Reset";
        buttonField.appendChild(reset);


        reset.addEventListener('click', function () { document.location.reload(true) }
        );

    }
});

function sleep(delay) {
    var start = new Date().getTime();
    while (new Date().getTime() < start + delay);
}

