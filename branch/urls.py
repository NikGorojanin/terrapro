from django.urls import path

from branch.views import ListView, CreateView, EditView, DeleteView

app_name = 'branch'

urlpatterns = [
    path('list', ListView.as_view(), name='list'),
    path('create', CreateView.as_view(), name='create'),
    path('edit/<int:branch_id>', EditView.as_view(), name='edit'),
    path('delete/<int:branch_id>', DeleteView.as_view(), name='delete'),
]
