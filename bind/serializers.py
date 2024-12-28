# bind/serializers.py
from rest_framework import serializers
from .models import TLD, Domain, DomainRecord


class TLDSerializer(serializers.ModelSerializer):
    class Meta:
        model = TLD
        fields = ['id', 'name', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class DomainRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DomainRecord
        fields = ['id', 'record_type', 'ip_address', 'priority', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class DomainSerializer(serializers.ModelSerializer):
    records = DomainRecordSerializer(many=True, read_only=True)
    tld_name = serializers.CharField(source='tld.name', read_only=True)
    full_domain = serializers.CharField(source='get_full_domain', read_only=True)

    class Meta:
        model = Domain
        fields = ['id', 'name', 'tld', 'tld_name', 'full_domain', 'records', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class BindConfigSerializer(serializers.Serializer):
    named_conf = serializers.CharField(read_only=True)
    zone_file = serializers.CharField(read_only=True)
