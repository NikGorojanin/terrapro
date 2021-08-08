from django.shortcuts import render, redirect, reverse
from django.views import View

from api.models import Branche

from branch.form import BranchForm


class ListView(View):
    def get(self, request):
        branches = Branche.objects.all()

        return render(request, 'branches.html', context={'branches': branches})


class CreateView(View):
    def get(self, request):
        form = BranchForm()

        return render(request, 'branch.html', context={'form': form})

    def post(self, request):
        form = BranchForm(request.POST)

        if not form.is_valid():
            return render(request, 'branch.html', context={'form': form})

        form.save()

        return redirect(reverse('branch:list'))


class EditView(View):
    def get(self, request, branch_id):
        branch = self._get_branch(branch_id)

        form = BranchForm(instance=branch)

        return render(request, 'branch.html', context={'form': form})

    def post(self, request, branch_id):
        branch = self._get_branch(branch_id)

        form = BranchForm(request.POST, instance=branch)

        if not form.is_valid():
            return render(request, 'branch.html', context={'form': form})

        form.save()

        return redirect(reverse('branch:list'))

    def _get_branch(self, branch_id):
        return Branche.objects.get(pk=branch_id)


class DeleteView(View):
    def post(self, request, branch_id):
        Branche.objects.get(pk=branch_id).delete()

        return redirect(reverse('branch:list'))
