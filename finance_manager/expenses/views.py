from django.shortcuts import render, redirect
from .models import Income, Expense
from .forms import IncomeForm, ExpenseForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.

def income_list(request):
    incomes = Income.objects.all()
    context = {
        'incomes':incomes
    }
    return render(request, 'expenses/income_list.html', context)

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/expense_list.html', {'expenses':expenses})


# def add_income(request):
#     if request.method == 'POST':
#         form = IncomeForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('income_list')
#     else:
#         form = IncomeForm()
#     return render(request, 'expenses/add_income.html', {'form':form})


def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form':form})


class IncomeCreateView(CreateView):
    model = Income
    fields = ['amount', 'description', 'category']
    template_name = 'expenses/add_income.html'
    success_url = reverse_lazy('income_list')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user to the logged-in user
        return super().form_valid(form)