from django.conf.urls import url
from django.urls import path

from post.views.list import PostList

app_name = 'post'

urlpatterns = [
    path('list', PostList.as_view(), name='list'),
]
