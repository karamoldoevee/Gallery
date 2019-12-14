from django.urls import include, path

from rest_framework import routers

from api import views


router = routers.DefaultRouter()

router.register(r'comments', views.CommentViewSet)

router.register(r'like', views.LikeViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]