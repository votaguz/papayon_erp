from django.db import models
from django.contrib.auth.models import User
    
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
    fax = models.CharField(max_length=20)
    address = models.CharField(max_length=140)
    name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    id_type = models.IntegerField(choices=ID_TYPE_CHOICES)
    id_number = models.CharField(max_length=140)
    reason = models.CharField(max_length=500)

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

    
class ContactEntity(models.Model):
    name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    id_number = models.CharField(max_length=140)
    phone = models.CharField(max_length=20)
    celphone = models.CharField(max_length=20)
    mail = models.CharField(max_length=140)
    provider = models.ForeignKey('ProviderEntity', related_name='contacts')
    password = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name
    pass

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
    
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
    order_number = models.IntegerField()
    purchase_date = models.DateField()
    delivery_date = models.DateField()
    provider = models.ForeignKey('ProviderEntity', related_name='purchase_orders')
    status = models.IntegerField(choices=STATUS_CHOICES)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return '%d' % self.order_number

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

