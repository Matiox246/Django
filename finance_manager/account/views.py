from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from expenses.models import Income

# Create your views here.

@login_required
def home(request):
    return render(request, 'registration/home.html')


class IncomeList(LoginRequiredMixin, ListView):
    queryset = Income.objects.all()
    template_name = "registration/home.html"
