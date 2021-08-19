import os
import csv
from datetime import datetime

from django.conf import settings
from django.core.management.base import BaseCommand

from api.models import Account
from account.models import User


class Command(BaseCommand):
    help = "Parse account file"

    def handle(self, *args, **options):
        file_path = os.path.join(settings.BASE_DIR, 'resources/fixtures', 'accounts.csv')

        print('Start {}'.format(datetime.now()))
        models_package = []
        if os.path.exists(file_path):
            with open(file_path) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')

                for row in csv_reader:
                    created_at = row[0]
                    updated_at = row[1]
                    barcode = row[2]
                    phone_number = row[3]
                    total_balance = row[4]
                    total_spent_monthly = row[5]
                    total_spent_yearly = row[6]
                    total_spent = row[7]
                    user_id = row[9]

                    account = Account(
                        created_at=created_at,
                        updated_at=updated_at,
                        barcode=barcode,
                        phone_number=phone_number,
                        total_balance=total_balance,
                        total_spent_monthly=total_spent_monthly,
                        total_spent_yearly=total_spent_yearly,
                        total_spent=total_spent
                    )

                    if user_id and user_id.isdigit():
                        user = User.objects.filter(id=user_id).first()

                        if user:
                            account.user = user
                    models_package.append(account)

                    if len(models_package) == 10000:
                        Account.objects.bulk_create(models_package)
                        print('saved {}'.format(datetime.now()))
                        models_package = []

                Account.objects.bulk_create(models_package)

        print('Done')
