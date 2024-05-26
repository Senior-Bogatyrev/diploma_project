from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from friendship.models import Friend, Follow, FriendshipRequest
from .forms import UserSearch


@login_required
def friends_list(request):
    friends = Friend.objects.friends(request.user)
    friends_count = len(friends)
    num_unrejected_requests = Friend.objects.unrejected_request_count(request.user)
    if request.method == 'POST':
        if request.POST.get('write_message'):
            ...
        elif request.POST.get('delete_friend'):
            user_id = request.POST.get('to_user_id')
            to_user = User.objects.get(id=user_id)
            from_user = request.user
            Friend.objects.remove_friend(from_user, to_user)
            Follow.objects.add_follower(to_user, from_user)
            return followers(request)

    return render(request,
                  'friends/friendsMain.html',
                  {'friends': friends,
                   'friends_count':friends_count,
                   'num_unrejected_requests':num_unrejected_requests})

@login_required
def search_users(request):
    form = UserSearch()
    user_list = False
    already_requested = {}
    background_color = {}

    if request.method == 'POST':
        if request.POST.get('search'):
            query_name = request.POST.get('search')
            user_list = User.objects.all()
            for term in query_name.split():
                user_list = user_list.filter(Q(first_name__icontains=term) | Q(last_name__icontains=term))
            for user in user_list:
                if FriendshipRequest.objects.filter(
                    from_user=request.user, to_user=user).exists():
                    already_requested[user.id] = 'Запрос отправлен'
                    background_color[user.id] = 'rgb(52, 205, 52)'
                elif FriendshipRequest.objects.filter(
                    from_user=user, to_user=request.user).exists():
                    already_requested[user.id] = 'Принять запрос'
                    background_color[user.id] = 'yellowgreen'
                elif Friend.objects.are_friends(user, request.user):
                    already_requested[user.id] = 'Удалить из друзей'
                    background_color[user.id] = 'red'
                else:
                    already_requested[user.id] = 'Добавить в друзья'
                    background_color[user.id] = 'grey'
            
        elif not request.POST.get('search') and request.POST.get('to_user'):
            user_id = request.POST.get('to_user')
            to_user = User.objects.get(id=user_id)
            from_user = request.user
            if request.POST.get('status_fr_request') == 'Добавить в друзья': 
                Friend.objects.add_friend(from_user, to_user)
            elif request.POST.get('status_fr_request') == 'Запрос отправлен':
                friend_request = FriendshipRequest.objects.get(from_user=from_user, to_user=to_user)
                friend_request.cancel()
            elif request.POST.get('status_fr_request') == 'Принять запрос':
                friend_request = FriendshipRequest.objects.get(from_user=to_user, to_user=from_user)
                friend_request.accept()
            elif request.POST.get('status_fr_request') == 'Удалить из друзей':
                Friend.objects.remove_friend(from_user, to_user)
                Follow.objects.add_follower(to_user, from_user)
                return followers(request)

    return render(request,
                  'friends/search_users.html', 
                  {'form':form,
                   'user_list':user_list,
                   'already_requested':already_requested,
                   'background_color':background_color
                   })


@login_required
def add_friend(request):
    num_unrejected_requests = Friend.objects.unrejected_request_count(request.user)
    friendship_requests = Friend.objects.requests(user=request.user)
    if request.POST:
        user_id = request.POST.get('user_id')
        to_user = User.objects.get(id=user_id)
        from_user = request.user
        if request.POST.get('add_friend'):
            friend_request = FriendshipRequest.objects.get(from_user=to_user, to_user=from_user)
            friend_request.accept()
            return friends_list(request)
        elif request.POST.get('follower'):
            friend_request = FriendshipRequest.objects.get(from_user=to_user, to_user=from_user)
            friend_request.cancel()
            Follow.objects.add_follower(to_user, from_user)
            return followers(request)
    return render(request,
                  'friends/friends_request_add.html',
                  {'friendship_requests': friendship_requests,
                   'num_unrejected_requests':num_unrejected_requests})

@login_required
def followers(request):
    num_unrejected_requests = Friend.objects.unrejected_request_count(request.user)
    followers = Follow.objects.followers(request.user)
    fol_count = len(followers)
    return render(request,
                  'friends/followers.html',
                  {'followers': followers,
                   'fol_count':fol_count,
                   'num_unrejected_requests':num_unrejected_requests})