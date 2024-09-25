from rest_framework import serializers
from .models import Store, Section, Template, Component

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = [
            'user', 'name', 'applied_date', 'created', 'updated',
        ]

class SectionSerializer(serializers.ModelSerializer):
    store = StoreSerializer(read_only = True)
    class Meta:
        model = Section
        fields = [
            'store', 'name',
        ]

class SectionTemplatesSerializer(serializers.ModelSerializer):
    section = SectionSerializer(read_only = True)
    class Meta:
        model = Template
        fields = [
            'name', 'section','active',
        ]

class ComponentSerializer(serializers.ModelSerializer):
    template = SectionTemplatesSerializer(read_only = True)
    class Meta:
        model = Component
        fields = [
            'name',
        ]