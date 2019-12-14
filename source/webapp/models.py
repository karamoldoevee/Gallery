from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    image = models.ImageField(upload_to='photo_images', null=False, blank=False, verbose_name='Фотография')
    signature = models.CharField(max_length=20, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата-время создания')
    likes = models.IntegerField(default=0, verbose_name='Лайки')
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, verbose_name='Автор')

class Comment(models.Model):
    text = models.TextField(max_length=2000, blank=False, verbose_name='Комментарий')
    image = models.ForeignKey('webapp.Photo', related_name='comments', on_delete=models.CASCADE,
                              verbose_name='Фотография')
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата-время создания')

    def __str__(self):
        return self.text

class Like(models.Model):
    image = models.ForeignKey('webapp.Photo', on_delete=models.CASCADE,
                              verbose_name='Фотография', related_name='like')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='like')