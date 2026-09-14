
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Post


def home(request):
    return HttpResponse('Hello, World!')


def about(request):
    return render(request, 'about.html', {
        'team': 'This is the Djangoblog team.'
    })


def post_list(request):
    posts = Post.objects.filter(is_published=True)
    query = request.GET.get('q', '').strip()
    if query:
        posts = posts.filter(
            Q(title__icontains=query)
            | Q(excerpt__icontains=query)
            | Q(content__icontains=query)
        )
    return render(request, 'home.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    return render(request, 'blog/post_detail.html', {
        'post': post
    })


def contact(request):
    return render(request, 'contact.html', {
        'abc': 'This is the Djangoblog team.'
    })