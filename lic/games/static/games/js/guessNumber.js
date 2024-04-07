let input = document.querySelector(".guess-num-input");
let btn = document.querySelector(".guess-num-button");
let check = document.querySelector(".result-check-out");
let help = document.querySelector(".result-help-out");
let count = document.querySelector(".result-count-out");
let helpDiv = document.querySelector(".guess-number-help");

let item = 0;
let randNum = 1 + Math.floor(Math.random() * 100);
let userNum;

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
    check.textContent = "Поздравляю! Вы угадали число";
    help.textContent = "В самый раз";
    item++;
    count.textContent = item;
    helpDiv.style.backgroundColor = "yellowgreen";
    helpDiv.style.color = "white";
  }
};