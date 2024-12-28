# bind/admin.py
from django.contrib import admin
from .models import TLD, Domain, DomainRecord


@admin.register(TLD)
class TLDAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('name', 'tld', 'get_full_domain', 'created_at')
    list_filter = ('tld',)
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(DomainRecord)
class DomainRecordAdmin(admin.ModelAdmin):
    list_display = ('domain', 'record_type', 'ip_address', 'priority', 'created_at')
    list_filter = ('record_type', 'domain')
    search_fields = ('domain__name', 'ip_address')
    readonly_fields = ('created_at', 'updated_at')
