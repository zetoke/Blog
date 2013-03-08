# Create your views here.
from blog.models import Posts, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf


def index(request):
    return render_to_response('index.html',
        {'categories': Category.objects.all(), 'posts': Posts.objects.all()[:5]})


def view_post(request, slug):
    context = {'post': get_object_or_404(Posts, slug=slug)}
    context.update(csrf(request))
    return render_to_response('view_post.html', context)


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html',
        {'category': category, 'posts': Posts.objects.filter(category=category)[:5]})
