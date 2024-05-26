from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render


@login_required
def main(request):
    return render(request, 'main/mainPage.html')

@login_required
def about(request):
    return render(request, 'main/about.html')

@login_required
def settings(request):
    return render(request, 'main/settings.html')

@login_required
def user(request, user_id):
    viewed_user = User.objects.get(id=user_id)
    return render(request, 'main/user.html',
                  {'viewed_user': viewed_user})