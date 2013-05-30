# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Guest'
        db.create_table(u'signup_guest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('second_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('first_surname', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('second_surname', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('balance', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=5, decimal_places=2)),
            ('no_pay', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('badge_name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('cabin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['logistics.Cabin'], null=True, blank=True)),
        ))
        db.send_create_signal(u'signup', ['Guest'])

        # Adding field 'Counselor.cabin'
        db.add_column(u'signup_counselor', 'cabin',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['logistics.Cabin'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Camper.assigned_counselor'
        db.delete_column(u'signup_camper', 'assigned_counselor_id')

        # Adding field 'Camper.cabin'
        db.add_column(u'signup_camper', 'cabin',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['logistics.Cabin'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Camper.counselor'
        db.add_column(u'signup_camper', 'counselor',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['signup.Counselor']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Guest'
        db.delete_table(u'signup_guest')

        # Deleting field 'Counselor.cabin'
        db.delete_column(u'signup_counselor', 'cabin_id')

        # Adding field 'Camper.assigned_counselor'
        db.add_column(u'signup_camper', 'assigned_counselor',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['signup.Counselor'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Camper.cabin'
        db.delete_column(u'signup_camper', 'cabin_id')

        # Deleting field 'Camper.counselor'
        db.delete_column(u'signup_camper', 'counselor_id')


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
            'Meta': {'ordering': "['age']", 'object_name': 'Generation'},
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
        u'signup.camper': {
            'Meta': {'ordering': "['first_surname']", 'object_name': 'Camper'},
            'badge_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'birth_cert_book': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'birth_cert_fol': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'birth_cert_num': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'birth_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'cabin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['logistics.Cabin']", 'null': 'True', 'blank': 'True'}),
            'counselor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['signup.Counselor']"}),
            'docs_signed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'father': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fathered'", 'null': 'True', 'to': u"orm['signup.Parent']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'first_surname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mother': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mothered'", 'null': 'True', 'to': u"orm['signup.Parent']"}),
            'no_pay': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'passport': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'registrar': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'second_surname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'special_case': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'})
        },
        u'signup.counselor': {
            'Meta': {'ordering': "['first_surname']", 'object_name': 'Counselor'},
            'badge_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'cabin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['logistics.Cabin']", 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'first_surname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_pay': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'second_surname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'small_group': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['logistics.SmallGroup']", 'unique': 'True'})
        },
        u'signup.guest': {
            'Meta': {'ordering': "['first_surname']", 'object_name': 'Guest'},
            'badge_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'cabin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['logistics.Cabin']", 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'first_surname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_pay': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'second_surname': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'signup.parent': {
            'Meta': {'ordering': "['first_surname']", 'object_name': 'Parent'},
            'birth_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'first_surname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'gov_id': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'second_surname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'})
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

    complete_apps = ['signup']