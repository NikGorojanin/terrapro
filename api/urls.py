from django.conf import settings
from django.urls import path, include

from api.views.account import AccountView

app_name = 'api'

urlpatterns = [
    path('accounts', AccountView.as_view(), name='accounts'),
]
