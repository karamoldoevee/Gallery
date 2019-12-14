from rest_framework import viewsets

from rest_framework.response import Response

from webapp.models import Comment, Like, Photo

from api.serializers import CommentSerializer, LikeSerializer

from rest_framework.permissions import AllowAny, DjangoModelPermissions, IsAuthenticated

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        elif self.request.method == 'POST':
            return [IsAuthenticated()]
        else:
            return [DjangoModelPermissions()]

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


    def create(self, request, *args, **kwargs):
        pk = request.data.get('image')
        image = Photo.objects.get(pk=pk)
        if self.queryset.filter(image=image):
            return Response({'error': 'Уже есть лайк'}, status=400)
        image.likes += 1
        image.save()
        return super(LikeViewSet, self).create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        pk = request.data.get('image')
        image = Photo.objects.get(pk=pk)
        if not self.queryset.filter(image=image):
            return Response({'error': 'Нету Лайка'}, status=400)
        image.likes -= 1
        image.save()
        return super(LikeViewSet, self).create(request, *args, **kwargs)
