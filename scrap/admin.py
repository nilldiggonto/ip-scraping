from django.contrib import admin
from .models import IpInfo,Protocols
# Register your models here.

@admin.register(IpInfo)
class IpInfoAdmin(admin.ModelAdmin):
    list_display = ('ip','port','country','up_time')
    horizontal_filter = ('protocol',)
    search_fields = ('ip','port','country','up_time')

@admin.register(Protocols)
class ProtocolsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)