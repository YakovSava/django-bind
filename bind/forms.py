# bind/forms.py
from django import forms
from .models import Domain, DomainRecord


class DomainForm(forms.ModelForm):
    class Meta:
        model = Domain
        fields = ['name', 'tld']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter domain name (e.g., test)',
            }),
            'tld': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            })
        }


class DomainRecordForm(forms.ModelForm):
    class Meta:
        model = DomainRecord
        fields = ['domain', 'record_type', 'ip_address', 'priority']
        widgets = {
            'domain': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'record_type': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'ip_address': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter IP address (e.g., 192.168.0.1)',
            }),
            'priority': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter priority (for MX records)',
            })
        }
