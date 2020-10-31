from django.db import models


class PostQuerySet(models.QuerySet):
    def get_category_posts(self, category):
        return self.filter(category=category)


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self.db)

    def get_category_posts(self, category):
        return self.get_queryset().get_category_posts(category)