from django.shortcuts import render
import random
from music.models import Music
from poems.models import Poem
from video.models import Video
from django.http import HttpResponse
from django.db.models import Count
from django.db.models import Q


def index(request):
    music_list = Music.objects.order_by('-uploaded_date')[:5]
    poem_list = Poem.objects.order_by('-uploaded_date')[:3]
    video_list = Video.objects.order_by('-uploaded_date')[:3]

    context = {
        'music_list': music_list,
        'poem_list': poem_list,
        'video_list': video_list,
    }

    return render(request, 'home/index.html', context)


def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        music_list = Music.objects.filter(Q(title__icontains=q) | Q(artist__icontains=q))
        poem_list = Poem.objects.filter(Q(title__icontains=q) | Q(author__icontains=q) | Q(text__icontains=q))
        video_list = Video.objects.filter(Q(title__icontains=q) | Q(artist__icontains=q))
        context = {'query': q, 'music_list': music_list, 'poem_list': poem_list, 'video_list': video_list}
        template = 'home/results.html'

    else:
        template = 'home/index.html'
        context = {}
    return render(request, template, context)


def about(request):
    return render(request, 'home/about.html')


def privacy(request):
    return render(request, 'home/privacy.html')


def promote(request):
    return render(request, 'home/promote.html')


def advertise(request):
    return render(request, 'home/advertise.html')
