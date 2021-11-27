import os
import xlsxwriter

from django.conf import settings

from report.settings.user_block import BlockUserReportSettings


class BlockUserReportGenerator:
    def __init__(self, report_data):
        self.report_data = report_data

        self.workbook = None
        self.worksheet = None
        self.report_settings = None

        self._cur_row = 0

    def generate(self):
        path = os.path.join(settings.DOCS_TMP_STORAGE, 'block_user_report.xlsx')

        self.workbook = xlsxwriter.Workbook(path)
        self.worksheet = self.workbook.add_worksheet()

        self.report_settings = BlockUserReportSettings(
            workbook=self.workbook,
            worksheet=self.worksheet
        )
        self.report_settings.set_column_width()

        self._write_title()

        self._write_data()

        self.workbook.close()

        return path

    def _write_title(self):
        for i, field in enumerate(self.report_settings.fields):
            self.worksheet.write(self._cur_row, i, field.title, self.report_settings.title_format)

        self._cur_row += 1

    def _write_data(self):
        for user in self.report_data:
            for i, field in enumerate(self.report_settings.fields):
                self.worksheet.write(self._cur_row, i, user.get(field.name), field.excel_format)
            self._cur_row += 1

        self._cur_row += 1
