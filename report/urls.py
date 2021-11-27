from django.urls import path

from report.views import AccountReportView, BlockedUserReportView


app_name = 'report'

urlpatterns = [
    path('accounts', AccountReportView.as_view(), name='accounts'),
    path('user_block', BlockedUserReportView.as_view(), name='user_block'),
]
