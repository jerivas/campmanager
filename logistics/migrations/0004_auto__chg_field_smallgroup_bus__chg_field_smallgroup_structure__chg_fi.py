# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'SmallGroup.bus'
        db.alter_column(u'logistics_smallgroup', 'bus', self.gf('django.db.models.fields.CharField')(default='', max_length=16))

        # Changing field 'SmallGroup.structure'
        db.alter_column(u'logistics_smallgroup', 'structure', self.gf('django.db.models.fields.CharField')(default='', max_length=16))

        # Changing field 'SmallGroup.cabin'
        db.alter_column(u'logistics_smallgroup', 'cabin', self.gf('django.db.models.fields.CharField')(default='', max_length=16))

    def backwards(self, orm):

        # Changing field 'SmallGroup.bus'
        db.alter_column(u'logistics_smallgroup', 'bus', self.gf('django.db.models.fields.CharField')(max_length=16, null=True))

        # Changing field 'SmallGroup.structure'
        db.alter_column(u'logistics_smallgroup', 'structure', self.gf('django.db.models.fields.CharField')(max_length=16, null=True))

        # Changing field 'SmallGroup.cabin'
        db.alter_column(u'logistics_smallgroup', 'cabin', self.gf('django.db.models.fields.CharField')(max_length=16, null=True))

    models = {
        u'logistics.smallgroup': {
            'Meta': {'ordering': "['generation']", 'object_name': 'SmallGroup'},
            'bus': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'cabin': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'generation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'structure': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        }
    }

    complete_apps = ['logistics']