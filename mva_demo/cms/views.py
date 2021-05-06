from django.shortcuts import get_object_or_404, render

from .models import Category, Song
# from .models import Song


def song_all(request):
    songs = Song.songs.all()
    return render(request, 'cms/home.html', {'songs': songs})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    songs = Song.objects.filter(category=category)
    return render(request, 'cms/songs/category.html', {'category': category, 'songs': songs})

def song_detail(request, slug):
    song = get_object_or_404(Song, slug=slug)
    return render(request, 'cms/songs/single.html', {'song': song, 'like': False})
