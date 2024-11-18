from django.contrib import admin
from .models import Expense, Income, Category

# Register your models here.

admin.site.register(Expense)
# admin.site.register(Income)
admin.site.register(Category)

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'category', 'date') 
    list_filter =  ['user','category']
    ordering = ['date', 'amount']
admin.site.register(Income, IncomeAdmin)
