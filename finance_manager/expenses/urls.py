from django.urls import path
from . import views
from .views import IncomeCreateView, ExpenseListView

urlpatterns = [
    path('incomes/', views.IncomeListView.as_view(), name='income_list'),
    path('expenses/<int:year>/<int:month>/', views.monthly_expense, name='monthly_expenses'),
    path('expenses/', ExpenseListView.as_view(), name='expense_list'),
    path('income/add/', IncomeCreateView.as_view(), name='add_income'),
    path('add_expense/', views.ExpensesCreateView.as_view(), name='add_expense')
]