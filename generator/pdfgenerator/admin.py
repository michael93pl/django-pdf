from django.contrib import admin
from pdfgenerator.models import Items
from django.shortcuts import redirect

class ItemsAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'first_name', 'last_name', 'birth', 'pesel', 'email', 'phone_no', 'street', 'city',
                    'code', 'date', 'view_link')
    search_fields = ('file_name', 'first_name', 'last_name', 'birth', 'pesel', 'email', 'phone_no', 'street', 'city',
                     'code', 'date')



admin.site.register(Items, ItemsAdmin)