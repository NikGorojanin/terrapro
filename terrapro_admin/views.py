from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render

from account.models import User
from api.models import Cite, Branche


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        users_count = User.objects.count()
        cities = Cite.objects.count()
        branches = Branche.objects.count()

        return render(
            request,
            template_name='home.html',
            context={
                'users_count': users_count,
                'branches': branches,
                'cities': cities,
            }
        )
