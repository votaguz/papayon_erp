# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProviderEntity'
        db.create_table(u'erp_providerentity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('provider_type', self.gf('django.db.models.fields.IntegerField')()),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('id_type', self.gf('django.db.models.fields.IntegerField')()),
            ('id_number', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'erp', ['ProviderEntity'])

        # Adding model 'CityEntity'
        db.create_table(u'erp_cityentity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'erp', ['CityEntity'])

        # Adding model 'DepartmentEntity'
        db.create_table(u'erp_departmententity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'erp', ['DepartmentEntity'])

        # Adding model 'CountryEntity'
        db.create_table(u'erp_countryentity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'erp', ['CountryEntity'])

        # Adding model 'ContactEntity'
        db.create_table(u'erp_contactentity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'erp', ['ContactEntity'])

        # Adding model 'DocumentEntity'
        db.create_table(u'erp_documententity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'erp', ['DocumentEntity'])

        # Adding model 'PurchaseOrderEntity'
        db.create_table(u'erp_purchaseorderentity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'erp', ['PurchaseOrderEntity'])

        # Adding model 'ItemEntity'
        db.create_table(u'erp_itementity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'erp', ['ItemEntity'])

        # Adding model 'ItemInPurchaseOrderEntity'
        db.create_table(u'erp_iteminpurchaseorderentity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'erp', ['ItemInPurchaseOrderEntity'])


    def backwards(self, orm):
        # Deleting model 'ProviderEntity'
        db.delete_table(u'erp_providerentity')

        # Deleting model 'CityEntity'
        db.delete_table(u'erp_cityentity')

        # Deleting model 'DepartmentEntity'
        db.delete_table(u'erp_departmententity')

        # Deleting model 'CountryEntity'
        db.delete_table(u'erp_countryentity')

        # Deleting model 'ContactEntity'
        db.delete_table(u'erp_contactentity')

        # Deleting model 'DocumentEntity'
        db.delete_table(u'erp_documententity')

        # Deleting model 'PurchaseOrderEntity'
        db.delete_table(u'erp_purchaseorderentity')

        # Deleting model 'ItemEntity'
        db.delete_table(u'erp_itementity')

        # Deleting model 'ItemInPurchaseOrderEntity'
        db.delete_table(u'erp_iteminpurchaseorderentity')


    models = {
        u'erp.cityentity': {
            'Meta': {'object_name': 'CityEntity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'erp.contactentity': {
            'Meta': {'object_name': 'ContactEntity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'erp.countryentity': {
            'Meta': {'object_name': 'CountryEntity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'erp.departmententity': {
            'Meta': {'object_name': 'DepartmentEntity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'erp.documententity': {
            'Meta': {'object_name': 'DocumentEntity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'erp.itementity': {
            'Meta': {'object_name': 'ItemEntity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'erp.iteminpurchaseorderentity': {
            'Meta': {'object_name': 'ItemInPurchaseOrderEntity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'erp.providerentity': {
            'Meta': {'object_name': 'ProviderEntity'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_number': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'id_type': ('django.db.models.fields.IntegerField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'provider_type': ('django.db.models.fields.IntegerField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'erp.purchaseorderentity': {
            'Meta': {'object_name': 'PurchaseOrderEntity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['erp']