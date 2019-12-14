from webapp.models import Photo, Comment

from rest_framework import serializers


class PhotoCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'created_at')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'created_at')


class PhotoSerializer(serializers.ModelSerializer):
    comments = PhotoCommentSerializer(many=True, read_only=True)
    class Meta:
        model = Photo
        fields = ('id', 'image', 'signature', 'author', 'created_at', 'comments')