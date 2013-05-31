# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ContactEntity'
        db.delete_table(u'erp_contactentity')

        # Adding field 'ContactProvider.session_token'
        db.add_column(u'erp_contactprovider', 'session_token',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=140),
                      keep_default=False)


        # Changing field 'PurchaseOrderEntity.modified_by'
        db.alter_column(u'erp_purchaseorderentity', 'modified_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['erp.ContactProvider']))

    def backwards(self, orm):
        # Adding model 'ContactEntity'
        db.create_table(u'erp_contactentity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'erp', ['ContactEntity'])

        # Deleting field 'ContactProvider.session_token'
        db.delete_column(u'erp_contactprovider', 'session_token')


        # Changing field 'PurchaseOrderEntity.modified_by'
        db.alter_column(u'erp_purchaseorderentity', 'modified_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['erp.ContactEntity']))

    models = {
        u'erp.cityentity': {
            'Meta': {'object_name': 'CityEntity'},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cities'", 'to': u"orm['erp.DepartmentEntity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'erp.contactprovider': {
            'Meta': {'object_name': 'ContactProvider'},
            'cellphone': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'document_id': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': u"orm['erp.ProviderEntity']"}),
            'session_token': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'erp.countryentity': {
            'Meta': {'object_name': 'CountryEntity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'erp.departmententity': {
            'Meta': {'object_name': 'DepartmentEntity'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'deparments'", 'to': u"orm['erp.CountryEntity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'erp.documententity': {
            'Meta': {'object_name': 'DocumentEntity'},
            'document_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'document_type': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'documents'", 'to': u"orm['erp.ProviderEntity']"}),
            'vigence': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'})
        },
        u'erp.itementity': {
            'Meta': {'object_name': 'ItemEntity'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'erp.iteminpurchaseorderentity': {
            'Meta': {'object_name': 'ItemInPurchaseOrderEntity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items_in_purchase_orders'", 'to': u"orm['erp.ItemEntity']"}),
            'purchase_order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': u"orm['erp.PurchaseOrderEntity']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'unit_price': ('django.db.models.fields.IntegerField', [], {})
        },
        u'erp.providerentity': {
            'Meta': {'object_name': 'ProviderEntity'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'providers'", 'to': u"orm['erp.CityEntity']"}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_number': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'id_type': ('django.db.models.fields.IntegerField', [], {}),
            'is_authorized': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'provider_type': ('django.db.models.fields.IntegerField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'erp.purchaseorderentity': {
            'Meta': {'object_name': 'PurchaseOrderEntity'},
            'delivery_date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'modified_orders'", 'null': 'True', 'to': u"orm['erp.ContactProvider']"}),
            'order_number': ('django.db.models.fields.IntegerField', [], {}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'purchase_orders'", 'to': u"orm['erp.ProviderEntity']"}),
            'purchase_date': ('django.db.models.fields.DateField', [], {}),
            'status': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['erp']