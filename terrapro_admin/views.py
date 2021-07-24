from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, template_name='home.html')
