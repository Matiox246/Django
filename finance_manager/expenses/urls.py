from django.urls import path
from . import views


urlpatterns = [
    path('incomes/', views.IncomeListView.as_view(), name='income_list'),
    path('expenses/<int:year>/<int:month>/', views.monthly_expense, name='monthly_expenses'),
    path('expenses/', views.monthly_expense, name='expense_list'),
    path('income/add/', views.IncomeCreateView.as_view(), name='add_income'),
    path('expenses/add', views.ExpensesCreateView.as_view(), name='add_expense'),
]