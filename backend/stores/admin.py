from django.contrib import admin
from .models import Section, Store, Template, Component, Plugin, StorePlugin

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name', 'user__name')
    list_filter = ['user']

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'store_id')
    search_fields = ('name',)
    list_filter = ['store_id__name'] 

@admin.register(Template)
class TempalteAdmin(admin.ModelAdmin):
    list_display = ('name', 'section_id')
    search_fields = ('name',)
    list_filter = ['section_id__name'] 

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    pass

@admin.register(Plugin)
class PluginAdmin(admin.ModelAdmin):
    pass

@admin.register(StorePlugin)
class StorePluginAdmin(admin.ModelAdmin):
    pass

# Register your models here.
