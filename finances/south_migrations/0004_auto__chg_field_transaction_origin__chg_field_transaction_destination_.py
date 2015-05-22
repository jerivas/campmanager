# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Transaction.origin'
        db.alter_column(u'finances_transaction', 'origin', self.gf('django.db.models.fields.CharField')(max_length=128, null=True))

        # Changing field 'Transaction.destination'
        db.alter_column(u'finances_transaction', 'destination', self.gf('django.db.models.fields.CharField')(max_length=128, null=True))

        # Changing field 'Transaction.transaction_date'
        db.alter_column(u'finances_transaction', 'transaction_date', self.gf('django.db.models.fields.DateField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Transaction.origin'
        raise RuntimeError("Cannot reverse this migration. 'Transaction.origin' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Transaction.destination'
        raise RuntimeError("Cannot reverse this migration. 'Transaction.destination' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Transaction.transaction_date'
        raise RuntimeError("Cannot reverse this migration. 'Transaction.transaction_date' and its values cannot be restored.")

    models = {
        u'finances.transaction': {
            'Meta': {'ordering': "['-transaction_date']", 'object_name': 'Transaction'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'transaction_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'transaction_type': ('django.db.models.fields.CharField', [], {'default': "'income'", 'max_length': '16'})
        }
    }

    complete_apps = ['finances']