from django.contrib import admin
from .models import Person, Musician, Album

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')  
    search_fields = ('first_name', 'last_name', 'email') 

@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'instrument')
    search_fields = ('first_name', 'last_name', 'instrument')

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'release_date', 'num_stars')
    list_filter = ('artist', 'release_date')
    search_fields = ('name', 'artist__first_name', 'artist__last_name')  
