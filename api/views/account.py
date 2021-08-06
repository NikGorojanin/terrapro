from rest_framework.views import APIView
from rest_framework.response import Response

from django_q.tasks import async_task, result

from api.serializers.account import AccountSerializer
from api.manager.account import AccountManager


class AccountView(APIView):

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        task_id = async_task(AccountManager.save_or_update, serializer.validated_data)

        return Response(status=200, data={'status': 'SUCCESS'})
