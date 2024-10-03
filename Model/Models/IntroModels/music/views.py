# from django.views.generic import ListView
# from .models import Person, Musician, Album

# class PersonListView(ListView):
#     model = Person
#     template_name = 'people_list.html' 
#     context_object_name = 'people'

# class MusicianListView(ListView):
#     model = Musician
#     template_name = 'musician_list.html'
#     context_object_name = 'musicians'

# class AlbumListView(ListView):
#     model = Album
#     template_name = 'albums_list.html' 
#     context_object_name = 'albums'


# views.py

# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Album, Musician
# from .forms import AlbumForm, MusicianForm

# # View cho danh sách album
# def album_list(request):
#     albums = Album.objects.all()
#     return render(request, 'album_list.html', {'albums': albums})

# # View cho chi tiết album
# def album_detail(request, album_id):
#     album = get_object_or_404(Album, id=album_id)
#     return render(request, 'album_detail.html', {'album': album})

# # View cho thêm album
# def album_create(request):
#     if request.method == "POST":
#         form = AlbumForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('album_list')
#     else:
#         form = AlbumForm()
#     return render(request, 'album_form.html', {'form': form})

# # View cho sửa album
# def album_update(request, album_id):
#     album = get_object_or_404(Album, id=album_id)
#     if request.method == "POST":
#         form = AlbumForm(request.POST, instance=album)
#         if form.is_valid():
#             form.save()
#             return redirect('album_detail', album_id=album.id)
#     else:
#         form = AlbumForm(instance=album)
#     return render(request, 'album_form.html', {'form': form})

# # View cho xóa album
# def album_delete(request, album_id):
#     album = get_object_or_404(Album, id=album_id)
#     if request.method == "POST":
#         album.delete()
#         return redirect('album_list')
#     return render(request, 'album_confirm_delete.html', {'album': album})

# # View cho bình chọn album
# def album_vote(request, album_id):
#     album = get_object_or_404(Album, id=album_id)
#     if request.method == "POST":
#         num_stars = request.POST.get('num_stars', 0)
#         album.num_stars += int(num_stars)
#         album.save()
#         return redirect('album_detail', album_id=album.id)

# # View cho danh sách nghệ sĩ
# def musician_list(request):
#     musicians = Musician.objects.all()
#     return render(request, 'musician_list.html', {'musicians': musicians})

# # View cho bình chọn nghệ sĩ
# def musician_vote(request, musician_id):
#     musician = get_object_or_404(Musician, id=musician_id)
#     if request.method == "POST":
#         pass
#     return render(request, 'musician_detail.html', {'musician': musician})


from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Musician,  Album
from .forms import MusicianForm, AlbumForm

class MusicianListView(ListView):
    model = Musician
    template_name = 'music/musician_list.html'
    context_object_name = 'musicians'

class MusicianCreateView(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'music/musician_form.html'
    success_url = reverse_lazy('musician_list')

class MusicianUpdateView(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'music/musician_form.html'
    success_url = reverse_lazy('musician_list')

class MusicianDeleteView(DeleteView):
    model = Musician
    template_name = 'music/musician_confirm_delete.html'
    success_url = reverse_lazy('musician_list')
class AlbumListView(ListView):
    model = Album
    template_name = 'music/album_list.html'
    context_object_name = 'albums'

class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'music/album_form.html'
    success_url = reverse_lazy('album_list')

class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'music/album_form.html'
    success_url = reverse_lazy('album_list')

class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'music/album_confirm_delete.html'
    success_url = reverse_lazy('album_list')