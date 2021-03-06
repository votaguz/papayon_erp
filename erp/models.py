from django.db import models
from django.contrib.auth.models import AbstractUser
    
class ProviderEntity(models.Model):

    PROVIDER_TYPE_CHOICES = (
        (1, 'Natural'),
        (2, 'Juridica'),
    )

    ID_TYPE_CHOICES = (
       (1, 'Cedula de Ciudadania'),
       (2, 'RUT'),
       (3, 'Pasaporte'),
    )

    city = models.ForeignKey('CityEntity', related_name='providers')
    provider_type = models.IntegerField(choices=PROVIDER_TYPE_CHOICES)
    phone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=140)
    name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140, blank=True, null=True)
    id_type = models.IntegerField(choices=ID_TYPE_CHOICES, blank=True, null=True)
    id_number = models.CharField(max_length=140, blank=True, null=True)
    reason = models.CharField(max_length=500, blank=True, null=True)
    nit = models.CharField(max_length=140, blank=True, null=True)
    is_authorized = models.BooleanField()


    def to_json_dict(self):
        data = {}

        data['city'] = self.city.name
        data['provider_type'] = self.get_provider_type_display()
        data['phone'] = self.phone
        data['fax'] = self.fax
        data['address'] = self.address
        data['name'] = self.name
        data['last_name'] = self.last_name
        data['id_type'] = self.get_id_type_display()
        data['id_number'] = self.id_number
        data['reason'] = self.reason
        data['is_authorized'] = self.is_authorized

        return data


    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

class CityEntity(models.Model):
    department = models.ForeignKey('DepartmentEntity', related_name='cities')
    name = models.CharField(max_length=140)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

class DepartmentEntity(models.Model):
    country = models.ForeignKey('CountryEntity', related_name='deparments')
    name = models.CharField(max_length=140)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'


class CountryEntity(models.Model):
    name = models.CharField(max_length=140)
    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'

    
class DocumentEntity(models.Model):
    DOCUMENT_TYPE_CHOICES = (
        (1, 'RUT'),
        (2, 'Certificado Bancario'),
        (3, 'Camara de Comercio'),
    )
    provider = models.ForeignKey('ProviderEntity', related_name='documents')
    document_type = models.IntegerField(choices=DOCUMENT_TYPE_CHOICES)
    vigence = models.CharField(max_length=140, blank=True, null=True)
    document_file = models.FileField(upload_to='providers_documents/', blank=True, null=True)
    def __unicode__(self):
        return self.document_type

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'


class PurchaseOrderEntity(models.Model):

    STATUS_CHOICES = (
        (1, 'En espera'),
        (2, 'Aceptada'),
        (3, 'Denegada'),
    )
    modified_by = models.ForeignKey('ContactProvider', related_name='modified_orders', blank=True, null=True)
    order_number = models.IntegerField()
    purchase_date = models.DateField()
    delivery_date = models.DateField(blank=True, null=True)
    provider = models.ForeignKey('ProviderEntity', related_name='purchase_orders')
    status = models.IntegerField(choices=STATUS_CHOICES)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return '%d' % self.order_number

    def to_json(self):
        data = {}


        data['order_number'] = self.order_number
        data['order_id'] = self.id
        data['purchase_date'] = self.purchase_date
        data['delivery_date'] = self.delivery_date
        data['provider'] = self.provider.name
        data['status'] = self.get_status_display()
        data['description'] = self.description

        return data

    class Meta:
        verbose_name = 'Orden de Compra'
        verbose_name_plural = 'Ordenes de Compra'

    
class ItemEntity(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'


class ItemInPurchaseOrderEntity(models.Model):

    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    purchase_order = models.ForeignKey('PurchaseOrderEntity', related_name='items')
    item = models.ForeignKey('ItemEntity', related_name='items_in_purchase_orders')


    def __unicode__(self):
        return self.item.name

    class Meta:
        verbose_name = 'Item en Orden'
        verbose_name_plural = 'Items en Ordenes'


class ContactProvider(models.Model):
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    document_id = models.CharField(max_length=140)
    provider = models.ForeignKey('ProviderEntity', related_name='contacts')
    phone = models.CharField(max_length=140)
    cellphone = models.CharField(max_length=140)
    #Login Information
    email = models.EmailField()
    password = models.CharField(max_length=140)
    session_token = models.CharField(max_length=140, blank=True, null=True)

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def to_json_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'document_id': self.document_id,
            'phone': self.phone,
            'cellphone': self.cellphone,
            'email'   : self.email,
            'provider_id': self.provider.id,
        }

    class Meta:
        verbose_name = 'Contacto Proveedor'
        verbose_name_plural = 'Contactos de Proveedores'



