# bind/utils.py
import os
import subprocess
from django.conf import settings
from django.template.loader import render_to_string


def get_serial():
    """Генерирует serial в формате YYYYMMDDNN"""
    from datetime import datetime
    return f"{datetime.now().strftime('%Y%m%d')}01"


def write_bind_configs():
    """Записывает все конфиги Bind9"""
    if not settings.BIND9_ENABLED:
        return

    from .models import Domain

    # Создаем директории если их нет
    os.makedirs(settings.BIND9_ZONES_DIR, exist_ok=True)

    # Собираем все конфиги доменов
    named_conf_content = []

    for domain in Domain.objects.all():
        # Генерируем zone file
        zone_content = render_to_string('bind/db.zone.j2', {
            'domain': domain,
            'records': domain.records.all(),
            'serial': get_serial()
        })

        # Записываем zone file
        zone_file_path = os.path.join(settings.BIND9_ZONES_DIR, f"db.{domain.get_full_domain()}")
        with open(zone_file_path, 'w') as f:
            f.write(zone_content)

        # Добавляем запись в named.conf.local
        named_conf_content.append(render_to_string('bind/named.conf.local.j2', {
            'domain': domain
        }))

    # Записываем named.conf.local
    with open(os.path.join(settings.BIND9_NAMED_CONF_DIR, 'named.conf.local'), 'w') as f:
        f.write('\n'.join(named_conf_content))

    # Перезагружаем Bind9
    try:
        subprocess.run(settings.BIND9_RELOAD_COMMAND.split(), check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error reloading Bind9: {e}")