from django import forms
from .models import Comment, Music, UserUpload


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'text')


class MusicForm(forms.ModelForm):

    class Meta:
        model = Music
        fields = ('artist', 'title', 'thumbnail', 'audio_file')


class UserMusicForm(forms.ModelForm):

    class Meta:
        model = UserUpload
        fields = ('artist', 'title', 'thumbnail', 'audio_file')
