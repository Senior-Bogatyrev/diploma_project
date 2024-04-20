let input = document.querySelector(".guess-num-input");
let btn = document.querySelector(".guess-num-button");
let check = document.querySelector(".result-check-out");
let help = document.querySelector(".result-help-out");
let count = document.querySelector(".result-count-out");
let helpDiv = document.querySelector(".guess-number-help");
let attempts = document.getElementById('attempts-count');

let item = 0;
let randNum = 1 + Math.floor(Math.random() * 100);
let userNum;

const modal = document.getElementById('modal');
const restartButton = document.getElementById('restart');
const exitButton = document.getElementById('exit');

function openModal() {
  modal.style.display = "block";
};

restartButton.addEventListener('click', function() {
  window.location.reload()
});

exitButton.addEventListener('click', function() {
  window.location.href = "../";
});


btn.onclick = function (evt) {
  evt.preventDefault();
  userNum = input.value;
  if (userNum > randNum) {
    check.textContent = "Пока что не угадали";
    help.textContent = "Ваше число, больше загаданного";
    item++;
    count.textContent = item;
  } else if (userNum < randNum) {
    check.textContent = "Пока что не угадали";
    help.textContent = "Ваше число, меньше загаданного";
    item++;
    count.textContent = item;
  } else {
    openModal();
    item++;
    attempts.innerText = 'Количество попыток - ' + item;
  }
}; 