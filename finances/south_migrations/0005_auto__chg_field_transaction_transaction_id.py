# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Transaction.transaction_id'
        db.alter_column(u'finances_transaction', 'transaction_id', self.gf('django.db.models.fields.CharField')(max_length=16, null=True))

    def backwards(self, orm):

        # Changing field 'Transaction.transaction_id'
        db.alter_column(u'finances_transaction', 'transaction_id', self.gf('django.db.models.fields.CharField')(default='000', max_length=16))

    models = {
        u'finances.transaction': {
            'Meta': {'ordering': "['-transaction_date']", 'object_name': 'Transaction'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'transaction_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'transaction_type': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['finances']