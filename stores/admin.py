from django.contrib import admin
from .models import Store

# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    # ...Store
    list_display = ('id', 'name','description',)
    list_filter = ['added']
    search_fields = ['description','name', ]
    list_editable = ['description',]
    list_display_links = ['name',]









admin.site.register(Store, StoreAdmin)
