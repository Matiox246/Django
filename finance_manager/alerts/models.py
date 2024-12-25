from django.db import models
from django.utils.timezone import now

from account.models import User

# Create your models here.

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_sent = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=100)
    alert_type = models.CharField(max_length=50)
    
    @property
    def time_since_sent(self):
        delta = now() - self.date_sent
        weeks, __ = divmod(delta.days, 7)
        days = delta.days
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, _ = divmod(remainder, 60)

        if weeks > 0:
            return f"{weeks} week ago"
        elif days > 0:
            return f"{days} days ago"
        elif hours > 0:
            return f"{hours} hours ago"
        elif minutes > 0:
            return f"{minutes} minutes ago"
        else:
            return "just now"
