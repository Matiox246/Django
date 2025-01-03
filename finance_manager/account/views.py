from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.db.models import Sum
from datetime import date

from account.models import User
from expenses.models import Income, Expense, ExpenseGoal, IncomeGoal
from alerts.models import Notification 
from alerts.views import get_alert_data
from expenses.views import get_save_of_month_data

from itertools import chain
from django.utils import timezone
from django.views import View

from expenses.models import Income 
from .mixins import FormValidMixins




@login_required
def recent_transacitions(request):

    user = request.user
    
    incomes = Income.objects.filter(user=request.user).order_by('date')
    expenses = Expense.objects.filter(user=request.user).order_by('date')


    # combine incomes & expenses
    combined_transactions = list(chain(
        incomes.values('amount', 'date', 'category', 'description'),
        expenses.values('amount', 'date', 'category', 'description')
    ))
    
    for transaction in combined_transactions:
        if transaction in incomes.values('amount', 'date', 'category', 'description'):
            transaction['transaction_type']= 'Income'
        else:
            transaction['transaction_type'] = 'Expense'

    # sort by date created
    combined_transactions.sort(key=lambda x: x['date'], reverse=True)

    count = request.GET.get('count', '5')  # default
    try:
        count = int(count)
    except ValueError:
        return HttpResponseBadRequest("Invalid count parameter")

    # get limited
    recent_transactions = combined_transactions[:count]

    now = timezone.now()
    current_month = now.month

    monthly_incomes = Income.objects.filter(date__month=current_month, user=user)
    monthly_expenses = Expense.objects.filter(date__month=current_month, user=user)

    monthly_expense_goal = ExpenseGoal.objects.filter(user=request.user).last()
    monthly_income_goal = IncomeGoal.objects.filter(user=request.user).last()

    total_imcomes_spent = monthly_incomes.aggregate(total=Sum('amount'))['total'] or 0
    total_expenses_spent = monthly_expenses.aggregate(total=Sum('amount'))['total'] or 0

    # display the precentage used of the set target value 
    value = monthly_expense_goal
    color = ""
    if value: 
        goal_value = value.amount
        percentage_spent = 100 - (round((total_expenses_spent / goal_value) * 100))
        if 100 >= percentage_spent > 70:
            color = '#2cba00'
        elif 70 >= percentage_spent > 50:
            color = '#a3ff00'
        elif 50 >= percentage_spent > 30:
            color = '#fff400'
        elif 30 >= percentage_spent > 10:
            color = '#ffa700'
        elif 10 >= percentage_spent > 0:
            color = '#ff0000'
        
    context_alert = get_alert_data(request.user)
    context_saved = get_save_of_month_data(request.user)

    context = {
        'recent_transactions': recent_transactions,
        

        'total_incomes': total_imcomes_spent,
        'total_expenses': total_expenses_spent,

        'expense_goal': monthly_expense_goal,
        'income_goal': monthly_income_goal,

        'percentage_spent': percentage_spent,
        'progress_color': color,

        **context_alert,
        **context_saved,
    }
    return render(request, 'registration/home.html', context)


class ExpenseGoalCreateView(FormValidMixins, CreateView):
    model = ExpenseGoal
    fields = ['amount']
    template_name = 'expenses/set_goal.html'
    success_url = reverse_lazy('account:home')

    def get_last_object_pk(self):
        last_pk = ExpenseGoal.objects.latest('created_at')
        print(last_pk)
        return ExpenseGoal.objects.latest('created_at')


class ExpenseGoalUpdateView(FormValidMixins, UpdateView):
    model = ExpenseGoal
    fields = ['amount']
    template_name = 'expenses/set_goal.html'
    success_url = reverse_lazy('account:home')
