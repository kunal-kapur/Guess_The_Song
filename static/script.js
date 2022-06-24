

JSON.parse

lyric_list = (info.song_lyrics);
let count = 1

const lyricField = document.getElementById("lyric-field");

const moreButton = document.getElementById("more");

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