import threading

from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers.tg_mailing import TelegramMailingSerializer
from api.manager.tg_mailing import TelegramMailing


class TelegramMailingView(APIView):

    def post(self, request):
        serializer = TelegramMailingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # task_id = async_task(TelegramMailing.run_mailing, serializer.validated_data)
        thread = threading.Thread(target=TelegramMailing.run_mailing, args=(serializer.validated_data,))
        thread.start()

        return Response(status=200, data={'status': 'SUCCESS'})
