from report.managers.base import BaseReportManager

from api.models import Account
from report.generators.accounts import AccountsReportGenerator


class AccountReportManager(BaseReportManager):
    def __init__(self, *args, **kwargs):
        super(AccountReportManager, self).__init__(*args, **kwargs)

    def build_report_generator(self):
        return AccountsReportGenerator(
            report_data=self._build_data_for_report(),
        )

    def get_report_name(self):
        return 'accounts_report - {}.xlsx'.format(self.daterange)

    def _build_data_for_report(self):
        accounts = Account.objects.filter(
            created_at__gte=self.date_from,
            created_at__lte=self.date_to
        )

        report_data = []

        for account in accounts:
            report_data.append({
                'id': account.id,
                'barcode': account.barcode,
                'phone': account.phone_number,
                'total_balance': account.total_balance,
                'total_spent_monthly': account.total_spent_monthly,
                'total_spent_yearly': account.total_spent_yearly,
                'total_spent': account.total_spent,
                'birthday': account.birthday.strftime('%d.%m.%Y') if account.birthday else '-',
                'created_at': account.created_at.strftime('%d.%m.%Y') if account.created_at else '-',
                'telegram_username': account.user.telegram_username if account.user else '-',
                'first_name': account.user.first_name if account.user else '-',
                'second_name': account.user.last_name if account.user else '-',
                'language': account.user.language if account.user else '-',
            })

        return report_data
