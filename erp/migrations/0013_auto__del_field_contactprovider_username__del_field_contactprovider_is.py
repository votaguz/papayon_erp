# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ContactProvider.username'
        db.delete_column(u'erp_contactprovider', 'username')

        # Deleting field 'ContactProvider.is_staff'
        db.delete_column(u'erp_contactprovider', 'is_staff')

        # Deleting field 'ContactProvider.is_active'
        db.delete_column(u'erp_contactprovider', 'is_active')

        # Deleting field 'ContactProvider.is_superuser'
        db.delete_column(u'erp_contactprovider', 'is_superuser')

        # Deleting field 'ContactProvider.last_login'
        db.delete_column(u'erp_contactprovider', 'last_login')

        # Deleting field 'ContactProvider.date_joined'
        db.delete_column(u'erp_contactprovider', 'date_joined')

        # Adding field 'ContactProvider.cellphone'
        db.add_column(u'erp_contactprovider', 'cellphone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=140),
                      keep_default=False)

        # Removing M2M table for field groups on 'ContactProvider'
        db.delete_table(db.shorten_name(u'erp_contactprovider_groups'))

        # Removing M2M table for field user_permissions on 'ContactProvider'
        db.delete_table(db.shorten_name(u'erp_contactprovider_user_permissions'))


        # Changing field 'ContactProvider.first_name'
        db.alter_column(u'erp_contactprovider', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=140))

        # Changing field 'ContactProvider.last_name'
        db.alter_column(u'erp_contactprovider', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=140))

        # Changing field 'ContactProvider.password'
        db.alter_column(u'erp_contactprovider', 'password', self.gf('django.db.models.fields.CharField')(max_length=140))
        # Adding field 'PurchaseOrderEntity.modified_by'
        db.add_column(u'erp_purchaseorderentity', 'modified_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='modified_orders', null=True, to=orm['erp.ContactEntity']),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'ContactProvider.username'
        raise RuntimeError("Cannot reverse this migration. 'ContactProvider.username' and its values cannot be restored.")
        # Adding field 'ContactProvider.is_staff'
        db.add_column(u'erp_contactprovider', 'is_staff',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ContactProvider.is_active'
        db.add_column(u'erp_contactprovider', 'is_active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'ContactProvider.is_superuser'
        db.add_column(u'erp_contactprovider', 'is_superuser',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ContactProvider.last_login'
        db.add_column(u'erp_contactprovider', 'last_login',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'ContactProvider.date_joined'
        db.add_column(u'erp_contactprovider', 'date_joined',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Deleting field 'ContactProvider.cellphone'
        db.delete_column(u'erp_contactprovider', 'cellphone')

        # Adding M2M table for field groups on 'ContactProvider'
        m2m_table_name = db.shorten_name(u'erp_contactprovider_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contactprovider', models.ForeignKey(orm[u'erp.contactprovider'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contactprovider_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'ContactProvider'
        m2m_table_name = db.shorten_name(u'erp_contactprovider_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contactprovider', models.ForeignKey(orm[u'erp.contactprovider'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contactprovider_id', 'permission_id'])


        # Changing field 'ContactProvider.first_name'
        db.alter_column(u'erp_contactprovider', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'ContactProvider.last_name'
        db.alter_column(u'erp_contactprovider', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'ContactProvider.password'
        db.alter_column(u'erp_contactprovider', 'password', self.gf('django.db.models.fields.CharField')(max_length=128))
        # Deleting field 'PurchaseOrderEntity.modified_by'
        db.delete_column(u'erp_purchaseorderentity', 'modified_by_id')


    models = {
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
            'cellphone': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'document_id': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': u"orm['erp.ProviderEntity']"})
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
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'modified_orders'", 'null': 'True', 'to': u"orm['erp.ContactEntity']"}),
            'order_number': ('django.db.models.fields.IntegerField', [], {}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'purchase_orders'", 'to': u"orm['erp.ProviderEntity']"}),
            'purchase_date': ('django.db.models.fields.DateField', [], {}),
            'status': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['erp']