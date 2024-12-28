# bind/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Domain, DomainRecord
from .utils import write_bind_configs

@receiver([post_save, post_delete], sender=Domain)
@receiver([post_save, post_delete], sender=DomainRecord)
def update_bind_configs(sender, instance, **kwargs):
    """Обновляет конфиги Bind9 при любых изменениях доменов или записей"""
    write_bind_configs()