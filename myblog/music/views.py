from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Music, Comment, MusicTag
from .forms import CommentForm, UserMusicForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.views.decorators.http import require_POST
import sys
# from analytics.mixin import ObjectViewedMixin
#
# from analytics.signals import object_viewed_signal
#
# sys.path.append("..")


class IndexView(generic.ListView):
    paginate_by = 6
    context_object_name = 'music_list'

    def get_queryset(self):

        return Music.objects.order_by('-uploaded_date')


def detail(request, slug):
    latest_posts = Music.objects.order_by('-uploaded_date')[:5]
    song = get_object_or_404(Music, slug=slug)

    p_views = Music.objects.filter(id=song.pk).update(page_views=F('page_views') + 1)

    comments = Comment.objects.filter(post=song)
    # a = ObjectViewedMixin

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = song
            comment.save()
            return HttpResponseRedirect(song.get_absolute_url())
    else:
        comment_form = CommentForm()

    context = {
        'latest_posts': latest_posts,
        'song': song,
        'comments': comments,
        'comment_form': comment_form,
    }
    # object_viewed_signal.send(song.__class__, instance=song, request=request)

    return render(request, 'music/detail.html', context)


@login_required
# @require_POST
def upload(request):
    if request.method == 'POST':
        AUDIO_FILE_TYPE = ['wav', 'mp3', 'ogg']
        IMAGE_FILE_TYPE = ['png', 'jpg', 'jpeg']
        print("1")
        form = UserMusicForm(request.POST, request.FILES)
        # genres = MusicTag.objects.all()
        print("2")
        # for x in form:
        #     print(x)
        if form.is_valid():
            print("3")
            form = form.save(commit=False)
            form.artist = request.POST.get('artist')
            form.title = request.POST.get('title')
            form.thumbnail = request.FILES.get('thumbnail')
            form.audio_file = request.FILES.get('audio_file')
            # form.music_tag = request.POST.get('music_tag')

            # form.music_tag = [x.tag_name for x in MusicTag.objects.all()]
            # movie_ids = []
            # for x in form.music_tag:
            #     movie_ids.append(int(request.POST.get(x))) if request.POST.get(x) else print("Go ahead")
            # # tag = MusicTag.objects.create(
            #     # tag_name
            # # )
            # for x in movie_ids:
            #     pass

            messages.success(request, 'has been successfully uploaded')
            print("4")

            if form.thumbnail.url.split('.')[-1].lower() not in IMAGE_FILE_TYPE:
                context = {
                    "form": form,
                    # 'genres': genres,
                    "message": "Image file must be PNG, JPG, or JPEG"
                }
                return render(request, "music/upload1.html", context)

            if form.audio_file.url.split('.')[-1].lower() not in AUDIO_FILE_TYPE:
                context = {
                    "form": form,
                    # 'genres': genres,
                    "message": "Audio file must be WAV, MP3, or OGG"
                }
                return render(request, "music/upload1.html", context)
            print("Remaining save")
            form.save()
            return redirect('/')
        else:
            print("No return")
            print(form.errors)
    else:
        form = UserMusicForm(request.POST or None, request.FILES or None)
        genres = MusicTag.objects.all()
        context = {
            "form": form,
            'genres': genres,
            "title": "Upload Your Song",
        }
        return render(request, "music/upload1.html", context)
