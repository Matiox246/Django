from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new_fname = form.cleaned_data['fname']
            new_lname = form.cleaned_data['lname']
            new_email = form.cleaned_data['email']
            new_meassage = form.cleaned_data['message']
            new_form = Contact(fname=new_fname, lname=new_lname, email=new_email, message=new_meassage)
            new_form.save()
        return redirect('contact')
    else:
        form = ContactForm()
        return render(request, 'contact/contact.html', {'form': form})