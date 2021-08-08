from django.shortcuts import render, redirect, reverse
from django.views import View

from api.models import Cite, Branche

from city.form import CityForm


class ListView(View):
    def get(self, request):
        cities = Cite.objects.all()

        return render(request, 'cities.html', context={'cities': cities})


class CreateView(View):
    def get(self, request):
        form = CityForm()

        return render(request, 'city.html', context={'form': form})

    def post(self, request):
        form = CityForm(request.POST)

        if not form.is_valid():
            return render(request, 'city.html', context={'form': form})

        form.save()

        return redirect(reverse('city:list'))


class EditView(View):
    def get(self, request, city_id):
        city = self._get_city(city_id)

        form = CityForm(instance=city)

        return render(request, 'city.html', context={'form': form})

    def post(self, request, city_id):
        city = self._get_city(city_id)

        form = CityForm(request.POST, instance=city)

        if not form.is_valid():
            return render(request, 'city.html', context={'form': form})

        form.save()

        return redirect(reverse('city:list'))

    def _get_city(self, city_id):
        return Cite.objects.get(pk=city_id)


class DeleteView(View):
    def post(self, request, city_id):
        Branche.objects.filter(cites_id=city_id).delete()
        Cite.objects.get(pk=city_id).delete()

        return redirect(reverse('city:list'))
