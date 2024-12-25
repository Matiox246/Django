from django.urls import path
from . import views


urlpatterns = [
    path('incomes/', views.monthly_incomes, name='income_list'),
    path('incomes/<int:year>/<int:month>/', views.monthly_incomes, name='monthly_incomes'),
    path('expenses/', views.monthly_expense, name='expense_list'),
    path('expenses/<int:year>/<int:month>/', views.monthly_expense, name='monthly_expenses'),
    path('incomes/add/', views.IncomeCreateView.as_view(), name='add_income'),
    path('expenses/add', views.ExpensesCreateView.as_view(), name='add_expense'),    
]