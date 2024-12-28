"""
URL configuration for djbind project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# django_bind/urls.py
from django.contrib import admin
from django.urls import path
from bind.views import (
    DomainListView,
    DomainCreateView,
    DomainRecordCreateView,
    DomainDeleteView,
    view_config
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DomainListView.as_view(), name='domain-list'),
    path('domain/add/', DomainCreateView.as_view(), name='domain-create'),
    path('record/add/', DomainRecordCreateView.as_view(), name='record-create'),
    path('domain/<int:domain_id>/config/', view_config, name='view-config'),
    path('domain/<int:pk>/delete/', DomainDeleteView.as_view(), name='domain-delete'),
]