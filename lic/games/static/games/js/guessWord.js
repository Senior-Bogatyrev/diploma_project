let all_letters = ['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н',
                   'О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь',
                   'Э','Ю','Я'];

function createButton() {
    let buttonsContainer = document.getElementById('buttons');
    for (let i =  0; i < all_letters.length; i++) {
        let elem = document.createElement('button');
        elem.id = all_letters[i];
        elem.className = 'letterBtn';
        elem.innerHTML = all_letters[i];
        buttonsContainer.appendChild(elem);
        elem.addEventListener('click', function() {
            guessingLetter(this);
        });
    }
};

function guessingLetter(button) {
    if (word.includes(button.id)) {
        let indecies = getIndicesOf(word, button.id);
        for (let i = 0; i < word.length; i++){
            if (indecies.includes(i)){
                document.getElementById(i).value = button.id;
            }
        }
        button.style.backgroundColor = 'lightgreen';
        button.setAttribute('disabled', true);
        lenWord -= indecies.length;
        if (lenWord == 0) {
            modal.style.display = 'block';
            stat.innerText = 'Вы победили!';
            fLine.innerText = `Правильное слово - ${word}`;
            sLine.innerText = 'Хотите сыграть еще раз?';
        };
    } else{
        attempts ++;
        if (attempts > 8){
            modal.style.display = 'block';
            stat.innerText = 'Вы проиграли!';
            fLine.innerText = `Правильное слово - ${word}`;
            sLine.innerText = 'Не сдавайтесь, у вас обязательно получится!';

        } else{
            button.style.backgroundColor = 'RGB(255,128,128)';
            button.setAttribute('disabled', true);
            let stageImg = document.getElementById('stage');
            stageImg.style.backgroundImage = 'url(/static/games/img/stage' + attempts + '.png)';
        }
    }
};

function getIndicesOf(word, letter) {
    let startIndex =  0;
    let index, indices = [];

    while ((index = word.indexOf(letter, startIndex)) > -1) {
        indices.push(index);
        startIndex = index + 1;
    }
    return indices;
};

function createLetterField(word) {
    let lettersContainer = document.getElementById('letters');

    for (let i =  0; i < word.length; i++) {
        let elem = document.createElement('input');
        elem.id = i;
        elem.className = 'inpLetters';
        elem.setAttribute('disabled', true);
        lettersContainer.appendChild(elem);
    }
};

let modal = document.getElementById('myModal');
let span = document.getElementsByClassName('close')[0];
let stat = document.getElementById('status');
let fLine = document.getElementById('firstLine');
let sLine = document.getElementById('secondLine');
let word = document.getElementById('word').innerHTML;
let guessedLetters = [];
let attempts =  0;
let lenWord = word.length;
createButton();
createLetterField(word);

span.onclick = function() {
    modal.style.display = 'none';
};

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = 'none';
    }
};

function refreshPage(){
    window.location.reload();
};