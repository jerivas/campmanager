# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Budget.active'
        db.add_column(u'finances_budget', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Budget.active'
        db.delete_column(u'finances_budget', 'active')


    models = {
        u'finances.budget': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Budget'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'balance': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'budget_id': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'finances.transaction': {
            'Meta': {'ordering': "['-transaction_date']", 'object_name': 'Transaction'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'budget': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finances.Budget']"}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'transaction_date': ('django.db.models.fields.DateField', [], {}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'transaction_type': ('django.db.models.fields.CharField', [], {'default': "'income'", 'max_length': '16'})
        }
    }

    complete_apps = ['finances']