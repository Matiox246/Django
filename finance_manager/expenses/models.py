from django.db import models
from django.utils import timezone
from account.models import User
# Create your models here.

class Income(models.Model):
    date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    category = models.ForeignKey("Category", verbose_name="Category", related_name="Income", on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"+{self.amount} on {self.date}"

class Expense(models.Model):
    date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey("Category", verbose_name="Category", related_name="Expense", on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    

    def __str__(self):
        return f"-{self.amount} on {self.date}"
    

class Category(models.Model):
    title = models.CharField("title", max_length=10)
    slug = models.SlugField("slug")

    def  __str__(self):
        return self.title


class IncomeGoal(models.Model):
    amount = models.IntegerField("amount")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.amount}"
    

class ExpenseGoal(models.Model):
    amount = models.IntegerField("amount")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount}"

class Saved(models.Model):
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=True, null=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE, null=True)
    percentage = models.IntegerField("percentage",null=True)

    
    def __str__(self):
        return f"{self.amount} in {self.date.month}"