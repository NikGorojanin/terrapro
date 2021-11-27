from report.settings.base import Field


class BlockUserReportSettings:
    ID = 'id'
    PHONE = 'phone'
    TELEGRAM_USERNAME = 'telegram_username'
    FIRST_NAME = 'first_name'
    SECOND_NAME = 'second_name'

    def __init__(self, workbook, worksheet):
        self.workbook = workbook
        self.worksheet = worksheet

        self.title_format = workbook.add_format({
            'bold': True,
            'align': 'center',
        })
        self.number_format = self.workbook.add_format({
            'num_format': '# ### ##0.00',
        })
        self.total_number_format = self.workbook.add_format({
            'num_format': '# ### ##0.00',
            'bold': True,
        })

        self.fields = [
            Field(name=self.ID, title='ID'),
            Field(name=self.TELEGRAM_USERNAME, title='Телеграм юзернейм'),
            Field(name=self.FIRST_NAME, title='Имя'),
            Field(name=self.SECOND_NAME, title='Фамилия'),
            Field(name=self.PHONE, title='Телефон'),
        ]

    def set_column_width(self):
        self.worksheet.set_column(1, 2, width=20)
        self.worksheet.set_column(3, 3, width=17)
        self.worksheet.set_column(4, 6, width=25)
