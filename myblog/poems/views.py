from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Poem, Comment
from django.views.generic.edit import FormMixin
from django.urls import reverse
from .forms import CommentForm
from django.utils import timezone
from django.http import HttpResponseRedirect


class IndexView(generic.ListView):
    paginate_by = 6
    context_object_name = 'poem_list'

    def get_queryset(self):

        return Poem.objects.order_by('-uploaded_date')


def detail(request, slug):
    latest_posts = Poem.objects.order_by('-uploaded_date')[:1]
    poem = get_object_or_404(Poem, slug=slug)
    comments = Comment.objects.filter(post=poem)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = poem
            comment.save()
            return HttpResponseRedirect(poem.get_absolute_url())
    else:
        comment_form = CommentForm()

    context = {
        'latest_posts': latest_posts,
        'poem': poem,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'poems/poem_detail.html', context)