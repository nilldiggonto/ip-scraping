from django.db import models

# Create your models here.
class Protocols(models.Model):
    name        = models.CharField(max_length=100,unique=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class IpInfo(models.Model):
    ip          = models.CharField(max_length=100,unique=True)
    port        = models.CharField(max_length=100)
    country     = models.CharField(max_length=100)
    up_time     = models.CharField(max_length=100)
    protocol    = models.ManyToManyField(Protocols)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.ip