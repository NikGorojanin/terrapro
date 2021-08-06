import logging
from datetime import datetime

from django.db import transaction

from api.models import Account
from account.models import User

log = logging.getLogger('account')


class AccountManager:
    @classmethod
    def save_or_update(cls, accounts_data):
        log.debug('Run add account with {} rows'.format(len(accounts_data)))
        print('Run add account with {} rows'.format(len(accounts_data)))

        for account_info in accounts_data:
            log.debug('Add account with data: {}'.format(account_info))

            if 'payload' not in account_info:
                continue

            payload = account_info.get('payload', {})
            phone = payload.get('phone_number')
            id_1c = payload.get('id')

            if not phone or not id_1c:
                continue

            total_balance = payload.get('total_balance', 0.0)
            total_spent_monthly = payload.get('total_spent_monthly', 0.0)
            total_spent_yearly = payload.get('total_spent_yearly', 0.0)
            total_spent = payload.get('total_spent', 0.0)
            birthday = payload.get('birthday')
            barcode = payload.get('barcode')

            if birthday != '':
                birthday = datetime.strptime(birthday, '%d-%m-%Y')
            else:
                birthday = None

            existing_account = Account.objects.filter(id_1c=id_1c).first()

            if existing_account:
                existing_account.phone = phone
                existing_account.barcode = barcode
                existing_account.total_balance = total_balance
                existing_account.total_spent_monthly = total_spent_monthly
                existing_account.total_spent_yearly = total_spent_yearly
                existing_account.total_spent = total_spent
                existing_account.birthday = birthday

                existing_account.save()
            else:
                user = User.get_or_create(id_1c, phone)
                account = Account(
                    user=user,
                    barcode=payload.get('barcode'),
                    phone_number=phone,
                    total_balance=total_balance if total_balance != '' else 0.0,
                    total_spent_monthly=total_spent_monthly if total_spent_monthly != '' else 0.0,
                    total_spent_yearly=total_spent_yearly if total_spent_yearly != '' else 0.0,
                    total_spent=total_spent if total_spent != '' else 0.0,
                    birthday=birthday,
                    id_1c=id_1c
                )
                account.save()
