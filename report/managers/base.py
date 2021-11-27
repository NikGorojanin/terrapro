from datetime import datetime


class BaseReportManager:
    def __init__(self, *args, **kwargs):
        self.daterange = None
        self.date_from = None
        self.date_to = None

        report_daterange = kwargs.get('report_daterange')

        if report_daterange:
            self.daterange = report_daterange[0]
            self.date_from, self.date_to = self._get_dates_from_daterange()

    def _get_dates_from_daterange(self):
        parts = self.daterange.split(' - ')

        return datetime.strptime(parts[0], '%d.%m.%Y'), datetime.strptime(parts[1], '%d.%m.%Y')
