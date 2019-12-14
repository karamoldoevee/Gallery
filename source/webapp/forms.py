from django import forms

from webapp.models import Photo, Comment



class ProductForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['image', 'signature', 'likes', 'author']

    def clean_signature(self):
        title = self.cleaned_data['signature']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['author']


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']