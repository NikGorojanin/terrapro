from django.urls import path

from post.views.list import PostList
from post.views.create import CreateView
from post.views.edit import EditView
from post.views.delete import DeleteView

app_name = 'post'

urlpatterns = [
    path('list', PostList.as_view(), name='list'),
    path('create', CreateView.as_view(), name='create'),
    path('edit/<int:post_id>', EditView.as_view(), name='edit'),
    path('delete/<int:post_id>', DeleteView.as_view(), name='delete'),
]
