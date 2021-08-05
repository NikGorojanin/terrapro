import requests

from django.conf import settings


class TelegramCacheManager:
    def __init__(self):
        self.values = {
            'chat_id': settings.TELEGRAM_CHAT_ID,
        }
        self._base_url = 'https://api.telegram.org/bot{}'.format(settings.BOT_TOKEN)

        self.files = None
        self.url = None

    def _send_request(self):
        r = requests.post(self.url, files=self.files, data=self.values)

        resp = r.json()

        if resp.get('ok'):
            return resp.get('result')

    def image_cache(self, image):
        if not image:
            return

        self.url = '{}{}'.format(self._base_url, '/sendPhoto')
        self.files = {
            'photo': image,
        }

        response = self._send_request()

        if not response:
            return

        photos = response.get('photo')

        if not photos:
            return

        return photos[0].get('file_id')

    def video_cache(self, video):
        if not video:
            return

        self.url = '{}{}'.format(self._base_url, '/sendVideo')
        self.files = {
            'video': video,
        }

        response = self._send_request()

        if not response:
            return

        return response.get('video', {}).get('file_id')

    def document_cache(self, document):
        if not document:
            return

        self.url = '{}{}'.format(self._base_url, '/sendDocument')
        self.files = {
            'document': document,
        }

        response = self._send_request()

        if not response:
            return

        return response.get('document', {}).get('file_id')
