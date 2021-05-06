from mva_demo.users.models import User
from django.db import models
from django.urls import reverse

class SongManager(models.Manager):
    def get_queryset(self):
        return super(SongManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('cms:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Song(models.Model):
    category = models.ForeignKey(Category, related_name='song', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='song_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='anonymous')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    songs = SongManager()

    class Meta:
        verbose_name_plural = 'Songs'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('cms:song_detail', args=[self.slug])

    def __str__(self):
        return self.title
