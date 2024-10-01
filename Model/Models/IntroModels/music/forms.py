# # forms.py

# from django import forms
# from .models import Album, Musician

# class AlbumForm(forms.ModelForm):
#     class Meta:
#         model = Album
#         fields = ['artist', 'name', 'release_date', 'num_stars']

# class MusicianForm(forms.ModelForm):
#     class Meta:
#         model = Musician
#         fields = ['first_name', 'last_name', 'instrument']


from django import forms
from .models import Album, Musician

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'instrument']
class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['artist', 'name', 'release_date', 'num_stars']