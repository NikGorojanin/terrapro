from django.conf.urls import url
from django.urls import path

from post.views.list import PostList
from post.views.post import PostView

app_name = 'post'

urlpatterns = [
    path('list', PostList.as_view(), name='list'),
    path('create', PostView.as_view(), name='create'),
]
