from django.shortcuts import render
from expenses.models import Income, Expense, IncomeGoal, ExpenseGoal
from django.utils import timezone
from .models import Notification
from django.db.models import Sum


# Create your views here.
def get_alert_data(user):
    now = timezone.now()
    current_month = now.month

    # Retrieve monthly incomes and expenses
    monthly_incomes = Income.objects.filter(date__month=current_month)
    monthly_expenses = Expense.objects.filter(date__month=current_month)

    total_incomes_spent = monthly_incomes.aggregate(total=Sum('amount'))['total'] or 0
    total_expenses_spent = monthly_expenses.aggregate(total=Sum('amount'))['total'] or 0

    # Retrieve the user's goals
    monthly_expense_goal = ExpenseGoal.objects.filter(user=user).last()
    monthly_income_goal = IncomeGoal.objects.filter(user=user).last()

    # Initialize percentage_spent with a default value
    percentage_spent = None

    if monthly_expense_goal:
        goal_value = monthly_expense_goal.amount
        if goal_value > 0:  # Avoid division by zero
            percentage_spent = 100 - (round((total_expenses_spent / goal_value) * 100))

    # Check recent notifications for the current month
    recent_alert = Notification.objects.filter(
        user=user,
        date_sent__month=now.month,
        date_sent__year=now.year
    )

    if percentage_spent is not None and percentage_spent <= 20:
        if not recent_alert.exists():
            notification_message = "You are close to your goal!"
            alert_type = "Expense Alert"
            Notification.objects.create(user=user, message=notification_message, alert_type=alert_type)

    # Retrieve all notifications for the user
    notifications = Notification.objects.filter(user=user)
    notification_count = notifications.count()

    # Add required data to context
    context = {
        'notifications': notifications,
        'notification_count': notification_count,
    }
    return context


def alerts(request):
    context = get_alert_data(request.user)
    return render(request, 'alerts/alerts.html', context)
