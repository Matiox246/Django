from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.db.models import Sum
from itertools import chain
from django.utils.timezone import now
from datetime import timedelta


from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from account.models import User
from .mixins import FieldMixin
from .models import Income, Expense, ExpenseGoal, IncomeGoal, Saved

# Create your views here.

# class ExpenseListView(LoginRequiredMixin, ListView):
#     model = Expense
#     template_name = 'expense/expense_list.html'
#     context_object_name = 'expenses'

class ExpensesCreateView(LoginRequiredMixin, FieldMixin, CreateView):
    model = Expense
    template_name = 'expenses/add_expense.html'
    success_url = reverse_lazy('expense_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# class IncomeListView(LoginRequiredMixin, ListView):
#     model = Income
#     template_name = 'expenses/income_list.html'
#     context_object_name = 'incomes'

class IncomeCreateView(LoginRequiredMixin, FieldMixin ,CreateView):
    model = Income
    fields = ['amount', 'description', 'category']
    template_name = 'expenses/add_income.html'
    success_url = reverse_lazy('income_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    


@login_required
def monthly_expense(request, year=None, month=None):
    username = request.GET.get('username')
    if username:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
    else: 
        user = request.user if request.user.is_authenticated else None

    if user:
        expenses = Expense.objects.filter(user=user).order_by('date')
        time_period = "All time"

        if year and month:
            expenses = expenses.filter(date__year=year, date__month=month)
            time_period =f"{year}-{month:02d}"
        else:
            time_period = "All Time"

        total_spent = expenses.aggregate(total=Sum('amount'))['total'] or 0
        value = ExpenseGoal.objects.filter(user=user).first() 
        if value: 
            goal_value = value.amount
            percentage_spent = round((total_spent / goal_value) * 100)

    context = {
        'user': user,
        'time_period': time_period,
        'total_spent': total_spent,
        'expenses': expenses,
        'goal_value': goal_value,
        'percentage_spent': percentage_spent,
    }
    return render(request, 'expenses/expense_list.html', context)


@login_required
def monthly_incomes(request, year=None, month=None):
    username = request.GET.get('username')
    if username:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
    else: 
        user = request.user if request.user.is_authenticated else None

    if user:
        incomes = Income.objects.filter(user=user).order_by('date')
        time_period = "All time"
        if year and month:
            incomes = incomes.filter(date__year=year, date__month=month)
            time_period =f"{year}-{month:02d}"
        elif not year or month:
            time_period = "All time"

        total_spent = incomes.aggregate(total=Sum('amount'))['total'] or 0
        

    context = {
        'user': user,
        'time_period': time_period,
        'total_spent': total_spent,
        'incomes': incomes,
        
    }
    return render(request, 'expenses/income_list.html', context)


def get_save_of_month_data(user):
    today = now().date()
    current_year = today.year
    current_month = today.month
    last_month = current_month - 2
    last_day_of_month = (today.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)

    user_expenses = Expense.objects.filter(user=user)
    monthly_expense = user_expenses.filter(date__month=current_month)
    total_monthly_expenses = monthly_expense.aggregate(total=Sum('amount'))['total'] or 0

    user_incomes = Income.objects.filter(user=user)
    monthly_incomes = user_incomes.filter(date__month=current_month)
    total_monthly_income = monthly_incomes.aggregate(total=Sum('amount'))['total'] or 0

    total_saved = total_monthly_income - total_monthly_expenses
    total_saved_percent = None
    if total_saved > 0:
        total_saved_percent = round(100 - ((total_monthly_expenses / total_monthly_income ) * 100), 1)

    current_month_save = Saved.objects.filter(date__month=current_month)
    if today == last_day_of_month and not current_month_save:
        # create saved object
        save_month_create = Saved.objects.create(user=user,
                                                    amount=total_saved,
                                                    date__month=current_month,
                                                    date__year=current_year,
                                                    percentage=total_saved_percent)
        
    saved_of_month = Saved.objects.filter(user=user,
                                           date__month=current_month,
                                           date__year = current_year).first()
    
    saved_of_last_month = Saved.objects.filter(user=user, date__month=last_month,date__year=current_year).first()

    context = {
        'total_saved':total_saved,
        'total_saved_percent':total_saved_percent,
        'saved_of_month': saved_of_month,
    }
    return context