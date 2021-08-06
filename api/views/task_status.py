from rest_framework.views import APIView
from rest_framework.response import Response

from django_q.tasks import async_task, result

from api.serializers.account import AccountSerializer
from api.manager.account import AccountManager


class TaskStateView(APIView):

    def post(self, request):
        task_id = request.data.get('task_id')
        print(request.data)
        res = result(task_id)

        return Response(status=200, data={'status': res})
