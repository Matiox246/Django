from django.contrib import admin
from .models import Expense, Income, Category, ExpenseGoal, IncomeGoal, Saved

# Register your models here.

admin.site.register(Expense)
# admin.site.register(Income)
admin.site.register(Category)
admin.site.register(ExpenseGoal)
admin.site.register(IncomeGoal)
admin.site.register(Saved)

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'category', 'date') 
    list_filter =  ['user','category']
    ordering = ['date', 'amount']
admin.site.register(Income, IncomeAdmin)
