from django.urls import path
from . import views

urlpatterns = [
    path("", views.fixed_costs_list, name="fixed_costs"),
    path('add/', views.add_fixed_cost, name="add")
]
