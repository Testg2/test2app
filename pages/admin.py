from django.contrib import admin
from .models import Contact
from django.contrib.auth.models import Group

# Register your models here.
# import and export python packages
from import_export.admin import ImportExportModelAdmin

# class ContactAdmin(admin.ModelAdmin):
class ContactAdmin(ImportExportModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'phone', 'email', 'text_message', 'gender')
    list_display_links = ('id', 'username',)
    list_editable = ('text_message',)
    search_fields = ('id', 'username', 'first_name', 'last_name', 'email', 'phone', 'text_message', 'gender')
    list_per_page = 5
    list_filter = ('gender',)


# display contact model in admin aread
admin.site.register(Contact, ContactAdmin)


# unregister model to display in admin area
admin.site.unregister(Group)