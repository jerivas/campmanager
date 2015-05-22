# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'SmallGroup', fields ['title']
        db.create_unique(u'logistics_smallgroup', ['title'])


    def backwards(self, orm):
        # Removing unique constraint on 'SmallGroup', fields ['title']
        db.delete_unique(u'logistics_smallgroup', ['title'])


    models = {
        u'logistics.smallgroup': {
            'Meta': {'ordering': "['generation']", 'object_name': 'SmallGroup'},
            'bus': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'cabin': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'generation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'structure': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        }
    }

    complete_apps = ['logistics']