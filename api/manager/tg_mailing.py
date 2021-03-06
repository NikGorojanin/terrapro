import time
import logging
from traceback import format_exc

from django.conf import settings

from account.models import User
from api.services.telegram import TelegramService

log = logging.getLogger(__name__)


class TelegramMailing:
    @classmethod
    def run_mailing(cls, mailing_data):
        telegram_service = TelegramService()

        log.debug('Run telegram mailing with {} users'.format(len(mailing_data)))

        for data in mailing_data:
            id_1c = data.get('id')
            text = data.get('text')

            if not id_1c or not text or len(text) == 0:
                continue

            user = User.objects.filter(id_1c=id_1c).first()

            if not user or not user.telegram_id:
                continue

            try:
                telegram_service.send_message(user.telegram_id, text)
            except Exception as exp:
                log.error(format_exc())

            time.sleep(settings.SECONDS_BETWEEN_SENDING_MESSAGE)
