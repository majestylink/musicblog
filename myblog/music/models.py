from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


class Music(models.Model):
	artist = models.CharField(max_length=300)
	title = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(default='', blank=True, unique=True)
	thumbnail = models.ImageField(blank=False)
	audio_file = models.FileField(default='')
	uploaded_date = models.DateTimeField(default=timezone.now)
	page_views = models.IntegerField(default=0)

	class Meta:
		ordering = ['-uploaded_date']

	def save(self):
		self.uploaded_date = timezone.now()
		self.slug = slugify(self.title)
		super(Music, self).save()

	def __str__(self):
		return self.title + ' by ' + self.artist

	def get_absolute_url(self):
		return reverse('music:detail', kwargs={'slug': self.slug})


class Comment(models.Model):
	name = models.CharField(max_length=200)
	text = models.TextField()
	post = models.ForeignKey(Music, on_delete=models.CASCADE)
	created_date = models.DateField(default=timezone.now)
	moderation = models.BooleanField(default=True)

	def __str__(self):
		return self.text


