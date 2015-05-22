# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Generation'
        db.delete_table(u'logistics_generation')

        # Adding field 'SmallGroup.structure'
        db.add_column(u'logistics_smallgroup', 'structure',
                      self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True),
                      keep_default=False)


        # Renaming column for 'SmallGroup.generation' to match new field type.
        db.rename_column(u'logistics_smallgroup', 'generation_id', 'generation')
        # Changing field 'SmallGroup.generation'
        db.alter_column(u'logistics_smallgroup', 'generation', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=1))
        # Removing index on 'SmallGroup', fields ['generation']
        db.delete_index(u'logistics_smallgroup', ['generation_id'])


        # Changing field 'SmallGroup.bus'
        db.alter_column(u'logistics_smallgroup', 'bus', self.gf('django.db.models.fields.CharField')(max_length=16, null=True))

        # Changing field 'SmallGroup.cabin'
        db.alter_column(u'logistics_smallgroup', 'cabin', self.gf('django.db.models.fields.CharField')(max_length=16, null=True))

    def backwards(self, orm):
        # Adding index on 'SmallGroup', fields ['generation']
        db.create_index(u'logistics_smallgroup', ['generation_id'])

        # Adding model 'Generation'
        db.create_table(u'logistics_generation', (
            ('age', self.gf('django.db.models.fields.PositiveIntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('structure', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'logistics', ['Generation'])

        # Deleting field 'SmallGroup.structure'
        db.delete_column(u'logistics_smallgroup', 'structure')


        # Renaming column for 'SmallGroup.generation' to match new field type.
        db.rename_column(u'logistics_smallgroup', 'generation', 'generation_id')
        # Changing field 'SmallGroup.generation'
        db.alter_column(u'logistics_smallgroup', 'generation_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['logistics.Generation']))

        # Changing field 'SmallGroup.bus'
        db.alter_column(u'logistics_smallgroup', 'bus', self.gf('django.db.models.fields.CharField')(max_length=32, null=True))

        # Changing field 'SmallGroup.cabin'
        db.alter_column(u'logistics_smallgroup', 'cabin', self.gf('django.db.models.fields.CharField')(max_length=32, null=True))

    models = {
        u'logistics.smallgroup': {
            'Meta': {'ordering': "['generation']", 'object_name': 'SmallGroup'},
            'bus': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'cabin': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'generation': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'structure': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['logistics']