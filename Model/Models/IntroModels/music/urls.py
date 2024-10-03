# # from django.urls import path
# # from .views import PersonListView, MusicianListView, AlbumListView

# # urlpatterns = [
# #     path('people/', PersonListView.as_view(), name='person-list'),
# #     path('musicians/', MusicianListView.as_view(), name='musician-list'),
# #     path('albums/', AlbumListView.as_view(), name='album-list'),
# # ]


# # urls.py

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('albums/', views.album_list, name='album_list'),
#     path('albums/<uuid:album_id>/', views.album_detail, name='album_detail'),
#     path('albums/create/', views.album_create, name='album_create'),
#     path('albums/<uuid:album_id>/edit/', views.album_update, name='album_update'),
#     path('albums/<uuid:album_id>/delete/', views.album_delete, name='album_delete'),
#     path('albums/<uuid:album_id>/vote/', views.album_vote, name='album_vote'),
#     path('musicians/', views.musician_list, name='musician_list'),
#     path('musicians/<uuid:musician_id>/vote/', views.musician_vote, name='musician_vote'),
# ]


from django.urls import path
from .views import MusicianListView, MusicianCreateView, MusicianUpdateView, MusicianDeleteView
from .views import AlbumListView, AlbumCreateView, AlbumUpdateView, AlbumDeleteView

urlpatterns = [
    path('musicians/', MusicianListView.as_view(), name='musician_list'),
    path('musicians/create/', MusicianCreateView.as_view(), name='musician_create'),
    path('musicians/<uuid:pk>/edit/', MusicianUpdateView.as_view(), name='musician_edit'),
    path('musicians/<uuid:pk>/delete/', MusicianDeleteView.as_view(), name='musician_delete'),
    
     path('albums/', AlbumListView.as_view(), name='album_list'),
    path('albums/create/', AlbumCreateView.as_view(), name='album_create'),
    path('albums/<uuid:pk>/edit/', AlbumUpdateView.as_view(), name='album_edit'),
    path('albums/<uuid:pk>/delete/', AlbumDeleteView.as_view(), name='album_delete'),
]
