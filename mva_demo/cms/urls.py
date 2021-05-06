from django.urls import path

from .views import song_all, song_detail, category_list

app_name = 'cms'

urlpatterns = [
    path('', song_all, name='song_all'),
    path('<slug:slug>', song_detail, name='song_detail'),
    path('category/<slug:category_slug>/', category_list, name='category_list'),
]