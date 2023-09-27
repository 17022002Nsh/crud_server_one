from django.urls import path
from .views import home, create_todo, edit_todo, delete_todo

urlpatterns = [
    path("", home, name='home'),
    path("create/", create_todo, name='cret'),
    path("edit/<int:pk>/", edit_todo, name="edit_todo"),
    path("delete/<int:pk>/", delete_todo, name="delet")
]
