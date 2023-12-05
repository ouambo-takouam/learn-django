from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Lead
from .forms import CustomUserCreationForm

class RegisterView(CreateView):
    template_name = "registration/register.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')

class LandingPageView(TemplateView):
    template_name = 'leads/landing.html'

class LeadListView(LoginRequiredMixin,ListView):
    model = Lead

class LeadDetailView(LoginRequiredMixin, DetailView):
    model = Lead

class LeadCreateView(LoginRequiredMixin, CreateView):
    model = Lead
    fields = ["first_name", "last_name", "age", "agent"]

    def get_success_url(self):
        return reverse('leads:lead_list')

    def form_valid(self, form):
        #TODO send email
        send_mail(
            subject='A lead has been created',
            message='Go to the site to see the new lead',
            from_email='test@test.com',
            recipient_list=['test2@test.com']
        )

        return super(LeadCreateView, self).form_valid(form)

class LeadUpdateView(LoginRequiredMixin, UpdateView):
    model = Lead
    fields = ["first_name", "last_name", "age", "agent"]
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('leads:lead_list')

class LeadDeleteView(LoginRequiredMixin, DeleteView):
    model = Lead
    success_url = reverse_lazy("leads:lead_list")

