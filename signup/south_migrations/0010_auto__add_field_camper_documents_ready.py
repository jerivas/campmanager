# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Camper.documents_ready'
        db.add_column(u'signup_camper', 'documents_ready',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Camper.documents_ready'
        db.delete_column(u'signup_camper', 'documents_ready')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'logistics.smallgroup': {
            'Meta': {'ordering': "['generation']", 'object_name': 'SmallGroup'},
            'bus': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'cabin': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'generation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'structure': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        },
        u'signup.camper': {
            'Meta': {'ordering': "['first_surname']", 'unique_together': "(('first_name', 'second_name', 'first_surname', 'second_surname'),)", 'object_name': 'Camper'},
            'badge_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'birth_cert_book': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'birth_cert_fol': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'birth_cert_num': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'birth_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'bus': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'cabin': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'counselor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['signup.Counselor']"}),
            'documents_ready': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'father': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fathered'", 'null': 'True', 'to': u"orm['signup.Parent']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'first_surname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'generation': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mother': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mothered'", 'null': 'True', 'to': u"orm['signup.Parent']"}),
            'no_pay': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'passport': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'perm_printed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'perm_signed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'reg_province': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'reg_state': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'registrar': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'registrar_position': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'registrar_title': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'second_surname': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'small_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['logistics.SmallGroup']", 'null': 'True', 'blank': 'True'}),
            'special_case': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'structure': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'})
        },
        u'signup.counselor': {
            'Meta': {'ordering': "['first_surname']", 'unique_together': "(('first_name', 'second_name', 'first_surname', 'second_surname'),)", 'object_name': 'Counselor'},
            'badge_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'bus': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'cabin': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'first_surname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'generation': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_pay': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'second_surname': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'small_group': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['logistics.SmallGroup']", 'unique': 'True'}),
            'structure': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'})
        },
        u'signup.guest': {
            'Meta': {'ordering': "['first_surname']", 'unique_together': "(('first_name', 'second_name', 'first_surname', 'second_surname'),)", 'object_name': 'Guest'},
            'badge_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'cabin': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'first_surname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_pay': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'second_surname': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'})
        },
        u'signup.parent': {
            'Meta': {'ordering': "['first_surname']", 'unique_together': "(('first_name', 'second_name', 'first_surname', 'second_surname'),)", 'object_name': 'Parent'},
            'birth_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'first_surname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'gov_id': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'known_as': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'second_surname': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'})
        },
        u'signup.payment': {
            'Meta': {'ordering': "['-receipt_id']", 'object_name': 'Payment'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'payment_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'receipt_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'})
        }
    }

    complete_apps = ['signup']