from django.shortcuts import render
import random
from django.core.paginator import Paginator
from . models import Video, Comment
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect

def videos_list(request):

    latest_videos_list = Video.objects.order_by('-uploaded_date')[:3]
    music_videos_list = Video.objects.get_category_posts('Music')[:5]
    movies_list = Video.objects.get_category_posts('Movies')[:5]

    context = {
        'latest_videos_list': latest_videos_list,
        'music_videos_list': music_videos_list,
        'movies_list': movies_list,
    }


    return render(request, 'video/video_list.html', context)


def music_videos(request):
    category = 'Music'
    category_list = Video.objects.get_category_posts('Music').order_by('-uploaded_date')

    paginator = Paginator(category_list, 2)
    page = request.GET.get('page')
    group = paginator.get_page(page)

    context = {
    'category_list': category_list,
    'category': category,
    'group': group,
    }

    return render(request, 'video/category_list.html', context)


def movies_videos(request):
    category = 'Movies'
    category_list = Video.objects.get_category_posts('Movies').order_by('-uploaded_date')

    paginator = Paginator(category_list, 2)
    page = request.GET.get('page')
    group = paginator.get_page(page)

    context = {
    'category_list': category_list,
    'category': category,
    'group': group,
    }

    return render(request, 'video/category_list.html', context)

def post_detail(request, slug):
    random_posts = random.sample(list(Video.objects.all()), 2)
    vid = get_object_or_404(Video, slug=slug)
    comments = Comment.objects.filter(post=vid)
    is_liked = False

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = vid
            comment.save()
            return HttpResponseRedirect(vid.get_absolute_url())
    else:
        comment_form = CommentForm()

    context = {
        'Video': Video,
        'vid': vid,
        'comments': comments,
        'comment_form': comment_form,
        'random_posts': random_posts,
    }
    return render(request, 'video/video_detail.html', context)