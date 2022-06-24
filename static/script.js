



lyric_list = (info.song_lyrics);
let count = 1

const correctArtist = info.song_artist;
const correctSongName = info.song_name;

const lyricField = document.getElementById("lyric-field");

const moreButton = document.getElementById("more");
const checkButton = document.getElementById("check");

const songInput = document.getElementById("song-input");


const artistInput = document.getElementById("artist-input");

moreButton.addEventListener("click", function () {
    if (count == (lyric_list).length) {
        let givenLyric = document.createElement("div");
        givenLyric.textContent = "END OF LYRICS";
        lyricField.appendChild(givenLyric);

    }
    else {
        let givenLyric = document.createElement("p");
        givenLyric.textContent = lyric_list[count];
        lyricField.appendChild(givenLyric);
    }
    count += 1;

})

checkButton.addEventListener("click", function () {
    bothCorrect = true
    if (songInput != correctSongName) {
        //bothCorrect = false;
    }

    if (artistInput != correctArtist) {
        //bothCorrect = false;
    }

    if (bothCorrect == true) {
        let correct = document.createElement("div")
        correct.style.color = 'green'
        correct.style.fontSize = '40px';
        correct.textContent = "CORRECT"
        console.log(document.querySelector(".container h1"));
        document.querySelector(".container .input-fields").insertBefore(correct, document.querySelectorAll(".container .input-fields" +
            " .text-input")[1]);
    }
})