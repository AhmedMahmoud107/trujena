from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    
    store_api_key = models.CharField(max_length=255, unique=True, blank=True)
    applied_date = models.DateTimeField(blank=True)
    
    notification_service_api_key = models.CharField(max_length=255, unique=True, blank=True)
    notification_service_auth_key = models.CharField(max_length=255, unique=True, blank=True)
    
    created = models.DateTimeField(blank=True, auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Visit(models.Model):
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    date = models.DateTimeField()

class StoreImage(models.Model):
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    url = models.ImageField(upload_to='images/')
    
    class Meta:
        unique_together = (('store_id', 'name'),)

class StorePlugin(models.Model):
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    is_active = models.BooleanField()
    settings = models.JSONField()
    
    def __str__(self):
        return self.name

class Plugin(models.Model):
    StorePlugin = models.ForeignKey(StorePlugin, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    page_url = models.FileField()
    code = models.TextField()
    settings = models.JSONField()
    
    def __str__(self):
        return self.name

class Section(models.Model):
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
    
class Template(models.Model):
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE)
    active = models.BooleanField()
    name = models.CharField(max_length=120)
    
    class Meta:
        unique_together = (('section_id', 'active'),)

    def __str__(self):
        return self.name
    
class Component(models.Model):
    template_id = models.ForeignKey(Template, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    settings = models.JSONField()

    def __str__(self):
        return self.name

