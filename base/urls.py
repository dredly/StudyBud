from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("room/<str:pk>/", views.room, name="room"),
    path("create-room/", views.create_room, name="create_room"),
    path("room/<str:pk>/update/", views.update_room, name="update_room"),
    path("room/<str:pk>/delete/", views.delete_room, name="delete_room"),
]
