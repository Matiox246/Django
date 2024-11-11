from django.shortcuts import render, redirect
from .models import FixedCost
from .forms import FixedCostForm

# Create your views here.\

def fixed_costs_list(request):
    fixed_costs = FixedCost.objects.all()
    context = {
        'fixed_costs': fixed_costs
    }
    return render(request, 'fixed_cost/fixed_cost_list.html', context)

def add_fixed_cost(request):
    if request.method == "POST":
        form = FixedCostForm(request.POST)
        # print(form.errors)
        if form.is_valid():
            form.save()
            schedule_choice = form.cleaned_data['schedule']
            custom_schedule = form.cleaned_data['custom_schedule'] if schedule_choice == 'custom' else None
            return redirect('fixed_costs')
    else:
        form = FixedCostForm()
    return render(request, 'fixed_cost/add_fixed_cost.html', {'form':form})
