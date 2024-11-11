from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            new_fname = form.cleaned_data("fname")
            new_lname = form.cleaned_data("lname")
            new_email = form.cleaned_data("email")
            new_meassage = form.cleaned_data("message")
            new_contact = Contact(fname=new_fname, lanme=new_lname, email=new_email, message=new_meassage)
            new_meassage.save()

        context = {
            'form': form
        }
        return render(request, "contact/cantact.html", context)