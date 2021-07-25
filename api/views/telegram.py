from rest_framework.views import APIView
from rest_framework.response import Response

from django_q.tasks import async_task

from api.serializers.tg_mailing import TelegramMailingSerializer
from api.manager.tg_mailing import TelegramMailing


class TelegramMailingView(APIView):

    def post(self, request):
        serializer = TelegramMailingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        async_task(TelegramMailing.run_mailing, serializer.validated_data)
        # TelegramMailing.run_mailing(serializer.validated_data)

        return Response(status=200)
