from django.contrib import admin
from pdfgenerator.models import Items

class ItemsAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'first_name', 'last_name', 'birth', 'pesel', 'email', 'phone_no', 'street', 'city',
                    'code', 'date',
                    'file_link')
    search_fields = ('file_name', 'first_name', 'last_name', 'birth', 'pesel', 'email', 'phone_no', 'street', 'city',
                     'code', 'date')

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['some_var'] ="something"
        return super(ItemsAdmin, self).changelist_view(request, extra_context=extra_context)

admin.site.register(Items, ItemsAdmin)