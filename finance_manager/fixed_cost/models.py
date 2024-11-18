from django.db import models

# Create your models here.

class FixedCost(models.Model):
    title = models.CharField("title", max_length=10)
    amount = models.IntegerField("amount")

    YEARLY = "yearly"
    MONTHLY = "monthly"
    WEEKLY = "weekly"
    DAILY = "daily"
    CUSTOM = "custom"
    SCHEDULES = {
        YEARLY : "yearly",
        MONTHLY : "monthly",
        WEEKLY : "weekly", 
        DAILY : "daily",
        CUSTOM : "custom"
        
    }
    schedule = models.CharField("schedule", choices=SCHEDULES, max_length=50, default=MONTHLY)
    

    PERMANANTLY = "permanantly"
    CUSTOM = "custom"
    DEADLINE =  {
        PERMANANTLY : "permanantly",
        CUSTOM : "custom"
    }
    deadline = models.CharField("deadline",max_length=50, choices=DEADLINE, default=PERMANANTLY)
    custom_deadline = models.DateField("custom_deadline", auto_now=False, auto_now_add=False, blank=True, null=True)
    

    def __str__(self):
        if self.schedule == 'custom':
            return f"Custom schedule is {self.schedule}"
        else:
            return self.title
        

    
    

    
    
    
    

