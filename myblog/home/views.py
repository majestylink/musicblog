from django.shortcuts import render
import random
from music.models import Music, UserUpload
from poems.models import Poem
from video.models import Video
from django.http import HttpResponse
from django.db.models import Count
from django.db.models import Q
import datetime


def index(request):
    week_ago = datetime.date.today() - datetime.timedelta(days=7)
    trends = Music.objects.filter(uploaded_date__gte=week_ago).order_by('-page_views')
    u_uploads = UserUpload.objects.order_by('-uploaded_date')[:10]

    music_list = Music.objects.order_by('-uploaded_date')[:5]
    poem_list = Poem.objects.order_by('-uploaded_date')[:3]
    video_list = Video.objects.order_by('-uploaded_date')[:3]

    first_in = music_list[0]
    others_in = music_list[1:3]

    context = {
        'music_list': music_list,
        'poem_list': poem_list,
        'video_list': video_list,
        'first_in': first_in,
        'others_in': others_in,
        'trends': trends,
        'u_uploads': u_uploads,
    }

    return render(request, 'home/new_index1.html', context)


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
