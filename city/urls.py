from django.urls import path

from city.views import ListView, CreateView, EditView, DeleteView

app_name = 'city'

urlpatterns = [
    path('list', ListView.as_view(), name='list'),
    path('create', CreateView.as_view(), name='create'),
    path('edit/<int:city_id>', EditView.as_view(), name='edit'),
    path('delete/<int:city_id>', DeleteView.as_view(), name='delete'),
]
