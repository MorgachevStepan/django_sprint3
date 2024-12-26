from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from .models import Post, Category


def filter_published_posts(queryset):
    return queryset.filter(
        is_published=True,
        pub_date__lte=now(),
        category__is_published=True
    )


def index(request):
    posts = filter_published_posts(
        Post.objects.all()
    ).order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'posts': posts})


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug, is_published=True)
    posts = filter_published_posts(Post.objects.filter(category=category))
    return render(
        request,
        'blog/category_posts.html',
        {'category': category, 'posts': posts}
    )


def post_detail(request, pk):
    post = get_object_or_404(
        Post,
        pk=pk,
        is_published=True,
        pub_date__lte=now(),
        category__is_published=True
    )
    return render(
        request,
        'blog/post_detail.html',
        {'post': post}
    )
