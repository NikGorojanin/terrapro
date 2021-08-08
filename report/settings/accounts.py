from report.settings.base import Field


class AccountReportSettings:
    ID = 'id'
    BARCODE = 'barcode'
    PHONE = 'phone'
    TOTAL_BALANCE = 'total_balance'
    TOTAL_SPENT_MONTHLY = 'total_spent_monthly'
    TOTAL_SPENT_YEARLY = 'total_spent_yearly'
    TOTAL_SPENT = 'total_spent'
    BIRTHDAY = 'birthday'
    CREATED_AT = 'created_at'
    TELEGRAM_USERNAME = 'telegram_username'
    FIRST_NAME = 'first_name'
    SECOND_NAME = 'second_name'
    LANGUAGE = 'language'

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
            Field(name=self.BARCODE, title='Баркод'),
            Field(name=self.PHONE, title='Телефон'),
            Field(name=self.TOTAL_BALANCE, title='Общий баланс', excel_format=self.number_format),
            Field(name=self.TOTAL_SPENT_MONTHLY, title='Всего потрачено за месяц', excel_format=self.number_format),
            Field(name=self.TOTAL_SPENT_YEARLY, title='Всего потрачено за год', excel_format=self.number_format),
            Field(name=self.TOTAL_SPENT, title='Всего потрачено за все время', excel_format=self.number_format),
            Field(name=self.BIRTHDAY, title='День рождения'),
            Field(name=self.CREATED_AT, title='Когда создан аккаунт'),
            Field(name=self.TELEGRAM_USERNAME, title='Телеграм юзернейм'),
            Field(name=self.FIRST_NAME, title='Имя'),
            Field(name=self.SECOND_NAME, title='Фамилия'),
            Field(name=self.LANGUAGE, title='Язык'),
        ]

    def set_column_width(self):
        self.worksheet.set_column(1, 2, width=20)
        self.worksheet.set_column(3, 3, width=17)
        self.worksheet.set_column(4, 6, width=25)
        self.worksheet.set_column(7, 8, width=18)
        self.worksheet.set_column(9, 11, width=20)
        self.worksheet.set_column(12, 12, width=10)

