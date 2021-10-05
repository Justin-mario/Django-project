from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_all_editors, name="editor_index"),
    path("<int:pk>/", views.get_an_editor, name="editor_detail"),
    path("create/", views.create_editor, name="create_editor"),
]