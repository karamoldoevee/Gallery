from django import forms

from webapp.models import Photo, Comment



class PhototForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['image', 'signature', 'likes', 'author']