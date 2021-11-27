from report.managers.base import BaseReportManager

from api.models import User
from report.generators.user_block import BlockUserReportGenerator


class BlockUserReportManager(BaseReportManager):
    def __init__(self, *args, **kwargs):
        super(BlockUserReportManager, self).__init__(*args, **kwargs)

    def build_report_generator(self):
        return BlockUserReportGenerator(
            report_data=self._build_data_for_report(),
        )

    def get_report_name(self):
            return 'user_block_report.xlsx'

    def _build_data_for_report(self):
        blocked_users = User.objects.filter(
            is_admin=-2,
        )

        report_data = []

        for user in blocked_users:
            report_data.append({
                'id': user.id,
                'phone': user.phone,
                'telegram_username': user.telegram_username or '-',
                'first_name': user.first_name or '-',
                'second_name': user.last_name or '-',
            })

        return report_data
