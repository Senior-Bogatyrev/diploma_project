from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, render, get_object_or_404
from friendship.models import Friend, Follow, Block
from .forms import UserSearch


@login_required
def friends_list(request):
    return render(request,
                  'friends/friendsMain.html')

@login_required
def search_users(request):
    form = UserSearch()
    user_list = False
    if request.method == 'POST':
        query_name = request.POST.get('search')
        user_list = User.objects.all()
        for term in query_name.split():
            user_list = user_list.filter(Q(first_name__icontains=term) | Q(last_name__icontains=term))

    return render(request,
                  'friends/search_users.html', {'form':form, 'user_list':user_list})

# @login_required
# def search_users(query):
#     ...

# def find_user_by_name(query_name):
#     qs = User.objects.all()
#     for term in query_name.split():
#         qs = qs.filter(Q(first_name__icontains=term) | Q(last_name__icontains=term))
#     return qs

# @login_required
# def post_list(request):
#     post_list = Post.published.all()
#     paginator = Paginator(post_list, 10)
#     page_number = request.GET.get('page', 1)
#     posts = paginator.page(page_number)

#     like_status = {}
#     for post in posts:
#         like_status[post.id] = post.user_liked(request.user)

#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.slug = slugify(post.title)
#             if 'published_news' in request.POST:
#                 post.status = 'PB'
#             elif 'draft_news' in request.POST:
#                 post.status = 'DF'
#             post.save()
#             form = PostForm()
#             return render(request,
#                           'news/post/list.html',
#                           {'posts': posts, 'form': form, 'like_status': like_status})
#     else:
#         form = PostForm()

#     return render(request,
#                   'news/post/list.html',
#                   {'posts': posts, 'form': form, 'like_status': like_status})