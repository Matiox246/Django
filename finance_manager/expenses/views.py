from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.db.models import Sum
from .mixins import FieldMixin

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from account.models import User


from .models import Income, Expense, expense_goal, income_goal
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
        expenses = Expense.objects.filter(user=user)
        time_period = "All time"

        if year and month:
            expenses = expenses.filter(date__year=year, date__month=month)
            time_period =f"{year}-{month:02d}"
        else:
            time_period = "All Time"

        total_spent = expenses.aggregate(total=Sum('amount'))['total'] or 0
        value = expense_goal.objects.filter(user=user).first() 
        if value: 
            goal_value = value.amount
            percentage_spent = round((total_spent / goal_value) * 100)
            if total_spent >= (goal_value * 80) / 100:
                print("ALARM: you are close to your monthly budget!")
        else:
            print("No expense goal found for this user.")

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
        incomes = Income.objects.filter(user=user)
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

    