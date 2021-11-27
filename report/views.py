from django.views import View
from django.http import HttpResponse

from report.managers.accounts import AccountReportManager
from report.managers.user_block import BlockUserReportManager


class AccountReportView(View):
    def post(self, request):
        manager = AccountReportManager(**request.POST)

        generator = manager.build_report_generator()

        path = generator.generate()

        file = open(path, 'rb')

        response = HttpResponse(file, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename="{file_name}"'.format(
            file_name=manager.get_report_name()
        )

        return response


class BlockedUserReportView(View):
    def post(self, request):
        manager = BlockUserReportManager(**request.POST)

        generator = manager.build_report_generator()

        path = generator.generate()

        file = open(path, 'rb')

        response = HttpResponse(file, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename="{file_name}"'.format(
            file_name=manager.get_report_name()
        )

        return response
