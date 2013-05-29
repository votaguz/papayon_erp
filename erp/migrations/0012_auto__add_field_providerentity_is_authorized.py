# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ProviderEntity.is_authorized'
        db.add_column(u'erp_providerentity', 'is_authorized',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ProviderEntity.is_authorized'
        db.delete_column(u'erp_providerentity', 'is_authorized')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'erp.cityentity': {
            'Meta': {'object_name': 'CityEntity'},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cities'", 'to': u"orm['erp.DepartmentEntity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'erp.contactentity': {
            'Meta': {'object_name': 'ContactEntity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'erp.contactprovider': {
            'Meta': {'object_name': 'ContactProvider'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'document_id': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': u"orm['erp.ProviderEntity']"}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
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
            'order_number': ('django.db.models.fields.IntegerField', [], {}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'purchase_orders'", 'to': u"orm['erp.ProviderEntity']"}),
            'purchase_date': ('django.db.models.fields.DateField', [], {}),
            'status': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['erp']