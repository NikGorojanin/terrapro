import logging
import threading

from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers.account import AccountSerializer
from api.manager.account import AccountManager

log = logging.getLogger('account')


class AccountView(APIView):

    def post(self, request):

        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        log.error('Accounts query with data: {}'.format(serializer.validated_data))

        # task_id = async_task(AccountManager.save_or_update, serializer.validated_data)
        thread = threading.Thread(target=AccountManager.save_or_update, args=(serializer.validated_data,))
        thread.start()

        return Response(status=200, data={'status': 'SUCCESS'})
