from django.urls import path

from api.views.account import AccountView
from api.views.telegram import TelegramMailingView
from api.views.task_status import TaskStateView

app_name = 'api'

urlpatterns = [
    path('accounts', AccountView.as_view(), name='accounts'),
    path('telegram/mailing', TelegramMailingView.as_view(), name='telegram'),
    path('task/status', TaskStateView.as_view(), name='task_status'),
]
