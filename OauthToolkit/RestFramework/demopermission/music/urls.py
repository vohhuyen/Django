from django.urls import path
from .views import SongView, SongReadWriteView, SongResourceScopeView

urlpatterns = [
    path('songs/', SongView.as_view(), name='song-list'),
    path('songs/readwrite/', SongReadWriteView.as_view(), name='song-readwrite'),
    path('songs/resourcescope/', SongResourceScopeView.as_view(), name='song-resourcescope'),
]
