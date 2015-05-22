# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Budget'
        db.create_table(u'finances_budget', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('budget_id', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('balance', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2, blank=True)),
        ))
        db.send_create_signal(u'finances', ['Budget'])

        # Adding model 'Transaction'
        db.create_table(u'finances_transaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('transaction_id', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('transaction_type', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('transaction_date', self.gf('django.db.models.fields.DateField')()),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('origin', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('destination', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('budget', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finances.Budget'])),
        ))
        db.send_create_signal(u'finances', ['Transaction'])


    def backwards(self, orm):
        # Deleting model 'Budget'
        db.delete_table(u'finances_budget')

        # Deleting model 'Transaction'
        db.delete_table(u'finances_transaction')


    models = {
        u'finances.budget': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Budget'},
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
            'transaction_type': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['finances']