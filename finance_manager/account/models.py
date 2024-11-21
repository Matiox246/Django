from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField(default=False, verbose_name="Membership type")
    premum_user = models.DateTimeField(default=timezone.now, verbose_name="Membership type")

    def is_premum_user(self):
        if self.premum_user > timezone.now():
            return True
        else:
            return False
