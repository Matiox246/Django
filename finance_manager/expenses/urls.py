from django.urls import path
from . import views
from .views import IncomeCreateView

urlpatterns = [
    path('incomes/', views.income_list, name='income_list'),
    path('expenses/', views.expense_list, name='expense_list'),
    path('income/add/', IncomeCreateView.as_view(), name='add_income'),
    path('add_expense/', views.add_expense, name='add_expense')
]