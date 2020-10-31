from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Music, Comment
from django.views.generic.edit import FormMixin
from django.urls import reverse
from .forms import CommentForm
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.db.models import F


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
    return render(request, 'music/detail.html', context)