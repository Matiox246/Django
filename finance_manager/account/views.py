from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django .contrib.auth.models import User
from expenses.models import Income

# Create your views here.

# @login_required
# def home(request):
#     incomes = Income.objects.all()
#     def get_queryset(self):
#         if self.request.user.is_superuser:
            
#             return incomes
#         else:
#             return Income.objects.filter(user=self.request.User)
#     return render(request, 'registration/home.html', {"incomes":incomes})


class IncomeList(LoginRequiredMixin, ListView):
    model = Income
    template_name = 'registration/home.html'
    context_object_name = 'incomes'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Income.objects.all()
        else:
            return Income.objects.filter(user=self.request.user)
        

