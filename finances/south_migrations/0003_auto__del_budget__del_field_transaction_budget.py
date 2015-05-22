# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Budget'
        db.delete_table(u'finances_budget')

        # Deleting field 'Transaction.budget'
        db.delete_column(u'finances_transaction', 'budget_id')


    def backwards(self, orm):
        # Adding model 'Budget'
        db.create_table(u'finances_budget', (
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('balance', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2, blank=True)),
            ('budget_id', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'finances', ['Budget'])

        # Adding field 'Transaction.budget'
        db.add_column(u'finances_transaction', 'budget',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['finances.Budget']),
                      keep_default=False)


    models = {
        u'finances.transaction': {
            'Meta': {'ordering': "['-transaction_date']", 'object_name': 'Transaction'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'transaction_date': ('django.db.models.fields.DateField', [], {}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'transaction_type': ('django.db.models.fields.CharField', [], {'default': "'income'", 'max_length': '16'})
        }
    }

    complete_apps = ['finances']