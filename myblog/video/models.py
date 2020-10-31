from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from .managers import PostManager


class Video(models.Model):
	
	CATEGORY_CHOICES = (
		('Music', 'Music'),
		('Movies', 'Movies'),
		)

	artist = models.CharField(max_length=200, unique=True)
	category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='Music')
	title = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(default='', blank=True, unique=True)
	thumbnail = models.ImageField(blank=False)
	video_file = models.FileField(default='')
	uploaded_date = models.DateTimeField(default=timezone.now)
	objects = PostManager()

	class Meta:
		ordering = ['-uploaded_date']

	def save(self):
		self.uploaded_date = timezone.now()
		self.slug = slugify(self.title)
		super(Video, self).save()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('video:detail', kwargs={'slug': self.slug})


class Comment(models.Model):
	name = models.CharField(max_length=200)
	text = models.TextField()
	post = models.ForeignKey(Video, on_delete=models.CASCADE)
	created_date = models.DateField(default=timezone.now)
	moderation = models.BooleanField(default=True)

	def __str__(self):
		return self.text
