# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SmallGroup'
        db.create_table(u'logistics_smallgroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('generation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['logistics.Generation'])),
            ('cabin', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('bus', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
        ))
        db.send_create_signal(u'logistics', ['SmallGroup'])

        # Adding model 'Generation'
        db.create_table(u'logistics_generation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('age', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('structure', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'logistics', ['Generation'])


    def backwards(self, orm):
        # Deleting model 'SmallGroup'
        db.delete_table(u'logistics_smallgroup')

        # Deleting model 'Generation'
        db.delete_table(u'logistics_generation')


    models = {
        u'logistics.generation': {
            'Meta': {'ordering': "['age']", 'object_name': 'Generation'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'structure': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'logistics.smallgroup': {
            'Meta': {'ordering': "['title']", 'object_name': 'SmallGroup'},
            'bus': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'cabin': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'generation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['logistics.Generation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['logistics']