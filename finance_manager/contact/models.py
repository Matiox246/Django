from django.db import models

# Create your models here.

class Contact(models.Model):
    fname = models.CharField("first name", max_length=10)
    lname = models.CharField("last name", max_length=50)
    email = models.EmailField("E-mail", max_length=254)
    message = models.CharField("message", max_length=200)
    time = models.DateField("time", auto_now_add=True, auto_now=False)

    def __str__(self):
        return f"{self.fname} {self.lname}"