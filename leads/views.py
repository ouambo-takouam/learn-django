from django.shortcuts import render

from .models import Lead
from .forms import LeadForm

def lead_list(request):
    leads = Lead.objects.all()

    return render(request, 'leads/lead_list.html', {
        'leads': leads
    })

def lead_detail(request, lead_id):
    lead = Lead.objects.get(pk=lead_id)

    return render(request, 'leads/lead_detail.html', {
        'lead': lead
    })

def lead_create(request):
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

    else:
        form = LeadForm()

    return render(request, 'leads/lead_create.html', {
        'form': form
    })
