from django.contrib import admin

from django.utils.translation import ugettext as _

from MIS import models


# Register your models here.

# @admin.register(models.Person)
class PersonView(admin.ModelAdmin):
    list_display = ('name', 'sex')
    search_fields = ('name',)
    fields = ('name', 'sex','info')


admin.site.site_header = _("Badger Admin Site")
admin.site.register(models.Company)
admin.site.register(models.Project)
admin.site.register(models.Contract)
admin.site.register(models.Contract_Company)
admin.site.register(models.Department)
admin.site.register(models.Person, PersonView)
