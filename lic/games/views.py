from django.shortcuts import render
from random import choice
from lic.settings import BASE_DIR
from django.contrib.auth.decorators import login_required


@login_required
def game_selection(request):
    return render(request, 'games/gameSelection.html')


@login_required
def guess_number(request):
    return render(request, 'games/guessNumber.html')


file_url = str(BASE_DIR) + '\games\static\games\words.txt'
with open(file_url, 'r', encoding='UTF-8') as f:
    words = [s.strip('\n') for s in f.read().split(',')]


@login_required
def guess_word(request):
    word = choice(words)
    return render(request, 'games/guessWord.html', {'word': word})