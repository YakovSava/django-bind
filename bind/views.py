# bind/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib import messages
from .models import Domain, TLD, DomainRecord
from .forms import DomainForm, DomainRecordForm


class DomainListView(ListView):
    model = Domain
    template_name = 'bind/domain_list.html'
    context_object_name = 'domains'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['domain_form'] = DomainForm()
        context['record_form'] = DomainRecordForm()
        return context


class DomainCreateView(SuccessMessageMixin, CreateView):
    model = Domain
    form_class = DomainForm
    template_name = 'bind/domain_form.html'
    success_url = reverse_lazy('domain-list')
    success_message = "Domain %(name)s was created successfully"


class DomainRecordCreateView(SuccessMessageMixin, CreateView):
    model = DomainRecord
    form_class = DomainRecordForm
    template_name = 'bind/record_form.html'
    success_url = reverse_lazy('domain-list')
    success_message = "Record was added successfully"

    def get_initial(self):
        initial = super().get_initial()
        domain_id = self.request.GET.get('domain')
        if domain_id:
            initial['domain'] = domain_id
        return initial


def view_config(request, domain_id):
    domain = Domain.objects.get(id=domain_id)
    context = {
        'domain': domain,
        'records': domain.records.all()
    }
    return render(request, 'bind/config_view.html', context)


class DomainDeleteView(DeleteView):
    model = Domain
    success_url = reverse_lazy('domain-list')
    template_name = 'bind/domain_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, f"Domain was deleted successfully")
        return super().delete(request, *args, **kwargs)
