from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.text import slugify
from .models import Post
from .forms import PostForm


def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            if 'published_news' in request.POST:
                post.status = 'PB'
            elif 'draft_news' in request.POST:
                post.status = 'DF'
            post.save()
            form = PostForm()
            return render(request,
                          'news/post/list.html',
                          {'posts': posts, 'form': form})
    else:
        form = PostForm()

    return render(request,
                  'news/post/list.html',
                  {'posts': posts, 'form': form})


def post_detail(request, id):
    post = get_object_or_404(Post,
                             id=id,
                             status=Post.Status.PUBLISHED)
    
    return render(request,
                  'news/post/detail.html',
                  {'post': post})

def draft(request):
    current_user = request.user
    draft_posts = Post.draft.filter(author=current_user)

    return render(request,
                  'news/post/draft.html',
                  {'draft_posts': draft_posts})

def draft_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('news:draft')
    return render(request, 'news/post/draft_post_delete.html', {'post': post})


def draft_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('news:draft')
    else:
        form = PostForm(instance=post)
    return render(request, 'news/post/draft_post_edit.html', {'form': form})

def draft_to_publish(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.status = 'PB'
        post.save()
        return redirect('news:post_list')
    return render(request, 'news/post/draft_to_publish.html', {'post': post})