from django.urls import path

from report.views import AccountReportView

app_name = 'report'

urlpatterns = [
    path('accounts', AccountReportView.as_view(), name='accounts'),
]
