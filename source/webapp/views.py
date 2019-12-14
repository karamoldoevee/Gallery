from webapp.models import Photo

from django.urls import reverse, reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class IndexView(ListView):
    model = Photo
    template_name = 'photo/index.html'
    context_object_name = 'photos'

    ordering = ['-created_at']

    paginate_by = 3

    paginate_orphans = 1


class PhotoView(DetailView):
    model = Photo
    template_name = 'photo/view.html'


class PhotoCreateView(CreateView):
    model = Photo
    template_name = 'photo/add.html'
    fields = ('image', 'signature', 'likes', 'author')

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})

class PhotoUpdateView(UpdateView):
    model = Photo
    template_name = 'photo/change.html'
    fields = ('image', 'signature', 'likes', 'author')
    context_object_name = 'photo'

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})


class PhotoDeleteView(DeleteView):
    template_name = 'photo/delete.html'

    model = Photo

    context_object_name = 'photo'

    success_url = reverse_lazy('webapp:index')
