from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from notifications.models import Notification
from notifications.signals import notify

from mva_demo.users.models import User

from .models import Category, Song


def song_all(request):
    songs = Song.songs.all()
    return render(request, 'cms/songs/index.html', {'songs': songs})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    songs = Song.objects.filter(category=category)
    return render(request, 'cms/songs/category.html', {'category': category, 'songs': songs})

def song_detail(request, slug):
    song = get_object_or_404(Song, slug=slug)
    user = User.objects.get(username=request.user)
    notif = user.notifications.filter(target_object_id=song.id).first()
    like = notif is not None and notif.verb=="like"
    return render(request, 'cms/songs/single.html', {'song': song, 'like': like})

@login_required
@require_POST
def like_song(request, slug):
    song = get_object_or_404(Song, slug=slug)
    sender = User.objects.get(username=request.user)
    notify.send(sender, recipient=song.created_by, target=song, verb='like')
    
    data = {"status": "ok", "target": song.slug, "action": "like"}
    return JsonResponse(data, safe=False)

@login_required
@require_POST
def unlike_song(request, slug):
    song = get_object_or_404(Song, slug=slug)
    sender = User.objects.get(username=request.user)
    notify.send(sender, recipient=song.created_by, target=song, verb='unlike')

    data = {"status": "ok", "target": song.slug, "action": "unlike"}
    return JsonResponse(data, safe=False)
