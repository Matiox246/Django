from django.urls import path
from . import views

urlpatterns = [
    path('incomes/', views.income_list, name='income_list'),
    path('expenses/', views.expense_list, name='expense_list'),
    path('add_income/', views.add_income, name='add_income'),
    path('add_expense/', views.add_expense, name='add_expense')
]