from django.contrib import admin
from pdfgenerator.models import Items

class ItemsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth', 'pesel', 'email', 'phone_no', 'street', 'city', 'code', 'date',
                    'file_link')
    search_fields = ('first_name', 'last_name', 'birth', 'pesel', 'email', 'phone_no', 'street', 'city', 'code', 'date')


admin.site.register(Items, ItemsAdmin)