from django.contrib import admin

from erp.models import ProviderEntity, CityEntity, DepartmentEntity, CountryEntity, DocumentEntity
from erp.models import PurchaseOrderEntity, ItemInPurchaseOrderEntity, ItemEntity, ContactProvider

class DocumentInline(admin.TabularInline):
    model = DocumentEntity
class ProviderAdmin(admin.ModelAdmin):

    list_display = ['city', 'provider_type', 'phone', 'fax', 'address', 'name', 'last_name', 'id_type', 'id_number', 'reason', 'is_authorized']
    inlines = [DocumentInline]

class PurchaseOrderAdmin(admin.ModelAdmin):
	list_display = ['order_number', 'purchase_date', 'delivery_date', 'provider', 'status']
	list_filter = ['provider', 'status']


admin.site.register(ProviderEntity, ProviderAdmin)
admin.site.register(CityEntity)
admin.site.register(DepartmentEntity)
admin.site.register(CountryEntity)
admin.site.register(DocumentEntity)
admin.site.register(ItemEntity)
admin.site.register(PurchaseOrderEntity, PurchaseOrderAdmin)
admin.site.register(ItemInPurchaseOrderEntity)
admin.site.register(ContactProvider)

