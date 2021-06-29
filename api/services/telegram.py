from django.conf import settings

import telegram


class TelegramService:
    def __init__(self):
        self._bot = telegram.Bot(settings.BOT_TOKEN)

    def send_message(self, chat_id, text, keyboard=None):
        self._bot.send_message(chat_id=chat_id, text=text, parse_mode='html', reply_markup=keyboard)
