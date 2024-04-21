from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def main(request):
    return render(request, 'main/mainPage.html')

@login_required
def about(request):
    return render(request, 'main/about.html')

@login_required
def message(request):
    return render(request, 'main/message.html')

@login_required
def settings(request):
    return render(request, 'main/settings.html')

@login_required
def games(request):
    return render(request, 'main/friends.html')