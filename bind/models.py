# bind/models.py
from django.db import models
from django.core.validators import RegexValidator

domain_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?$',
    message='Domain name must contain only letters, numbers, and hyphens, and cannot start or end with a hyphen.'
)

class TLD(models.Model):
    name = models.CharField(
        max_length=63,
        unique=True,
        validators=[domain_validator],
        help_text="Top Level Domain (e.g. 'com', 'org', 'net')"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Top Level Domain"
        verbose_name_plural = "Top Level Domains"

class Domain(models.Model):
    name = models.CharField(
        max_length=63,
        validators=[domain_validator],
        help_text="Domain name without TLD"
    )
    tld = models.ForeignKey(
        TLD,
        on_delete=models.CASCADE,
        related_name='domains'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['name', 'tld']
        verbose_name = "Domain"
        verbose_name_plural = "Domains"

    def __str__(self):
        return f"{self.name}.{self.tld}"

    def get_full_domain(self):
        return f"{self.name}.{self.tld}"

class DomainRecord(models.Model):
    RECORD_TYPES = [
        ('A', 'A'),
        ('AAAA', 'AAAA'),
        ('CNAME', 'CNAME'),
        ('MX', 'MX'),
        ('TXT', 'TXT'),
    ]

    domain = models.ForeignKey(
        Domain,
        on_delete=models.CASCADE,
        related_name='records'
    )
    record_type = models.CharField(
        max_length=5,
        choices=RECORD_TYPES,
        default='A'
    )
    ip_address = models.GenericIPAddressField(
        help_text="IP address for the record"
    )
    priority = models.IntegerField(
        default=0,
        help_text="Priority for MX records"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.domain} - {self.record_type} - {self.ip_address}"

    class Meta:
        verbose_name = "Domain Record"
        verbose_name_plural = "Domain Records"