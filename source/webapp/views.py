from django.http import HttpResponseRedirect
from webapp.models import Photo

from django.urls import reverse, reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

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


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    template_name = 'photo/add.html'
    fields = ('image', 'signature', 'likes')

    def form_valid(self, form):
        self.object = Photo.objects.create(author=self.request.user, image=form.cleaned_data['image'],
                                           signature=form.cleaned_data['signature'])

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})

class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Photo

    permission_required = 'webapp.change_photo'
    permission_denied_message = "Доступ запрещён"

    template_name = 'photo/change.html'
    fields = ('image', 'signature', 'likes', 'author')
    context_object_name = 'photo'

    def has_permission(self):
        return super().has_permission() or self.photo_author(self.request.user)

    def photo_author(self, user):
        return self.get_object().author == user

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})


class PhotoDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'photo/delete.html'

    model = Photo

    permission_required = 'webapp.delete_photo'
    permission_denied_message = "Доступ запрещён"

    context_object_name = 'photo'

    success_url = reverse_lazy('webapp:index')

    def has_permission(self):
        return super().has_permission() or self.photo_author(self.request.user)

    def photo_author(self, user):
        return self.get_object().author == user