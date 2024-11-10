from django.contrib import admin
from .models import FixedCost
# Register your models here.

class FixedCostAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'schedule')
    list_filter = ()
    search_fields = ('title')
    ordering = ('amount')
    