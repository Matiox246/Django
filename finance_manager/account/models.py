from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import datetime
# Create your models here.

class User(AbstractUser):
    is_author = models.BooleanField(default=False, verbose_name="Is Author")
    premum_user = models.DateTimeField(default=timezone.now, verbose_name="Is Premum Until")

    def is_premum_user(self):
        if self.premum_user and self.premum_user > timezone.now():
            return True
        else:
            return False
    is_premum_user.boolean = True
    is_premum_user.short_description = "IS PREMUM USER"