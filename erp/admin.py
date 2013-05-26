from django.contrib import admin

from erp.models import ProviderEntity, CityEntity, DepartmentEntity, CountryEntity, DocumentEntity


class DocumentInline(admin.TabularInline):
    model = DocumentEntity
class ProviderAdmin(admin.ModelAdmin):
    inlines = [DocumentInline]

admin.site.register(ProviderEntity, ProviderAdmin)
admin.site.register(CityEntity)
admin.site.register(DepartmentEntity)
admin.site.register(CountryEntity)
admin.site.register(DocumentEntity)
