from django.urls import path
from webapp.views import IndexView, PhotoView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', PhotoView.as_view(), name='photo_view'),
    path('product/add/', PhotoCreateView.as_view(), name='photo_add'),
    path('product/<int:pk>/change/', PhotoUpdateView.as_view(), name='photo_change'),
    path('product/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    ]