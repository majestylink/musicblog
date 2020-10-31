from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


class Poem(models.Model):
	title = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(default='', blank=True, unique=True)
	author = models.CharField(max_length=200, unique=True)
	thumbnail = models.ImageField(blank=True)
	uploaded_date = models.DateTimeField(default=timezone.now)
	text = RichTextUploadingField()

	class Meta:
		ordering = ['-uploaded_date']

	def save(self):
		self.uploaded_date = timezone.now()
		self.slug = slugify(self.title)
		super(Poem, self).save()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('poem:detail', kwargs={'slug': self.slug})




class Comment(models.Model):
	name = models.CharField(max_length=200)
	text = models.TextField()
	post = models.ForeignKey(Poem, on_delete=models.CASCADE)
	created_date = models.DateField(default=timezone.now)
	moderation = models.BooleanField(default=True)

	def __str__(self):
		return self.text
