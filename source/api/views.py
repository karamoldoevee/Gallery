from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Photo, Comment

from api.serializers import PhotoSerializer, CommentSerializer

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, DjangoModelPermissions, IsAuthenticated

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    # authentication_classes = SessionAuthentication
    # permission_classes = IsAuthenticated


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # authentication_classes = SessionAuthentication
    # permission_classes = IsAuthenticated

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        elif self.request.method == 'POST':
            return [IsAuthenticated()]
        else:
            return [DjangoModelPermissions()]
