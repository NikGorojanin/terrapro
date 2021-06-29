from django.conf import settings
from django.urls import path, include

from api.views.account import AccountView
from api.views.telegram import TelegramMailingView

app_name = 'api'

urlpatterns = [
    path('accounts', AccountView.as_view(), name='accounts'),
    path('telegram/mailing', TelegramMailingView.as_view(), name='telegram'),
]
