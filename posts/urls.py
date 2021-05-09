from django.contrib import admin
from django.urls import path

from .views import PostViewSet, UserAPIView


urlpatterns = [
    path('posts', PostViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    
    path('posts/<str:pk>', PostViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),

    path('user', UserAPIView.as_view())

]
