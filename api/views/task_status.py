from rest_framework.views import APIView
from rest_framework.response import Response

from django_q.tasks import async_task, result

from api.serializers.account import AccountSerializer
from api.manager.account import AccountManager


class TaskStateView(APIView):

    def post(self, request):
        return Response(status=200, data={'status': 'OK'})
