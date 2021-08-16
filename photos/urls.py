from django.urls import path, include
from . import views

urlpatterns = [
    path('photos/', views.list_photos),
    path('photos/<int:pk>/like', views.like_photo),
    path('photos/<int:pk>/dislike', views.dislike_photo)
]

