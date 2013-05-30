# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Generation'
        db.create_table(u'logistics_generation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('age', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('structure', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'logistics', ['Generation'])


        # Renaming column for 'SmallGroup.generation' to match new field type.
        db.rename_column(u'logistics_smallgroup', 'generation', 'generation_id')
        # Changing field 'SmallGroup.generation'
        db.alter_column(u'logistics_smallgroup', 'generation_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['logistics.Generation']))
        # Adding index on 'SmallGroup', fields ['generation']
        db.create_index(u'logistics_smallgroup', ['generation_id'])


    def backwards(self, orm):
        # Removing index on 'SmallGroup', fields ['generation']
        db.delete_index(u'logistics_smallgroup', ['generation_id'])

        # Deleting model 'Generation'
        db.delete_table(u'logistics_generation')


        # Renaming column for 'SmallGroup.generation' to match new field type.
        db.rename_column(u'logistics_smallgroup', 'generation_id', 'generation')
        # Changing field 'SmallGroup.generation'
        db.alter_column(u'logistics_smallgroup', 'generation', self.gf('django.db.models.fields.PositiveIntegerField')())

    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'logistics.bus': {
            'Meta': {'object_name': 'Bus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'responsible': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['signup.Counselor']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'logistics.cabin': {
            'Meta': {'object_name': 'Cabin'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'logistics.generation': {
            'Meta': {'object_name': 'Generation'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'structure': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'logistics.smallgroup': {
            'Meta': {'ordering': "['title']", 'object_name': 'SmallGroup'},
            'bus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['logistics.Bus']", 'null': 'True', 'blank': 'True'}),
            'cabin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['logistics.Cabin']", 'null': 'True', 'blank': 'True'}),
            'generation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['logistics.Generation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'signup.counselor': {
            'Meta': {'ordering': "['first_surname']", 'object_name': 'Counselor'},
            'badge_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'first_surname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_pay': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'second_surname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'small_group': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['logistics.SmallGroup']", 'unique': 'True'})
        },
        u'signup.payment': {
            'Meta': {'ordering': "['-payment_date']", 'object_name': 'Payment'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'payment_date': ('django.db.models.fields.DateField', [], {}),
            'receipt_id': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['logistics']