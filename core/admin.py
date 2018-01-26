from django.contrib import admin

from .models import Unit

class UnitAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'slug', 'acronym', 'created', 'modified']
    search_fields = ['name', 'slug', 'acronym']
    list_filter = ['created', 'modified']

admin.site.register(Unit, UnitAdmin)