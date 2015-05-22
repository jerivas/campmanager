# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Counselor.bus'
        db.alter_column(u'signup_counselor', 'bus', self.gf('django.db.models.fields.CharField')(default='', max_length=16))

        # Changing field 'Counselor.badge_name'
        db.alter_column(u'signup_counselor', 'badge_name', self.gf('django.db.models.fields.CharField')(default='', max_length=64))

        # Changing field 'Counselor.structure'
        db.alter_column(u'signup_counselor', 'structure', self.gf('django.db.models.fields.CharField')(default='', max_length=16))

        # Changing field 'Counselor.second_surname'
        db.alter_column(u'signup_counselor', 'second_surname', self.gf('django.db.models.fields.CharField')(default='', max_length=64))

        # Changing field 'Counselor.second_name'
        db.alter_column(u'signup_counselor', 'second_name', self.gf('django.db.models.fields.CharField')(default='', max_length=64))

        # Changing field 'Counselor.cabin'
        db.alter_column(u'signup_counselor', 'cabin', self.gf('django.db.models.fields.CharField')(default='', max_length=16))

        # Changing field 'Camper.second_surname'
        db.alter_column(u'signup_camper', 'second_surname', self.gf('django.db.models.fields.CharField')(default='', max_length=64))

        # Changing field 'Camper.occupation'
        db.alter_column(u'signup_camper', 'occupation', self.gf('django.db.models.fields.CharField')(default='', max_length=32))

        # Changing field 'Camper.state'
        db.alter_column(u'signup_camper', 'state', self.gf('django.db.models.fields.CharField')(default='', max_length=3))

        # Changing field 'Camper.passport'
        db.alter_column(u'signup_camper', 'passport', self.gf('django.db.models.fields.CharField')(default='', max_length=16))

        # Changing field 'Camper.cabin'
        db.alter_column(u'signup_camper', 'cabin', self.gf('django.db.models.fields.CharField')(default='', max_length=16))

        # Changing field 'Camper.province'
        db.alter_column(u'signup_camper', 'province', self.gf('django.db.models.fields.CharField')(default='', max_length=32))

        # Changing field 'Camper.bus'
        db.alter_column(u'signup_camper', 'bus', self.gf('django.db.models.fields.CharField')(default='', max_length=16))

        # Changing field 'Camper.badge_name'
        db.alter_column(u'signup_camper', 'badge_name', self.gf('django.db.models.fields.CharField')(default='', max_length=64))

        # Changing field 'Camper.structure'
        db.alter_column(u'signup_camper', 'structure', self.gf('django.db.models.fields.CharField')(default='', max_length=16))

        # Changing field 'Camper.registrar'
        db.alter_column(u'signup_camper', 'registrar', self.gf('django.db.models.fields.CharField')(default='', max_length=256))

        # Changing field 'Camper.second_name'
        db.alter_column(u'signup_camper', 'second_name', self.gf('django.db.models.fields.CharField')(default='', max_length=64))

        # Changing field 'Payment.notes'
        db.alter_column(u'signup_payment', 'notes', self.gf('django.db.models.fields.CharField')(default='', max_length=256))

        # Changing field 'Guest.badge_name'
        db.alter_column(u'signup_guest', 'badge_name', self.gf('django.db.models.fields.CharField')(default='', max_length=64))

        # Changing field 'Guest.second_surname'
        db.alter_column(u'signup_guest', 'second_surname', self.gf('django.db.models.fields.CharField')(default='', max_length=64))

        # Changing field 'Guest.second_name'
        db.alter_column(u'signup_guest', 'second_name', self.gf('django.db.models.fields.CharField')(default='', max_length=64))

        # Changing field 'Guest.cabin'
        db.alter_column(u'signup_guest', 'cabin', self.gf('django.db.models.fields.CharField')(default='', max_length=16))

        # Changing field 'Parent.province'
        db.alter_column(u'signup_parent', 'province', self.gf('django.db.models.fields.CharField')(default='', max_length=32))

        # Changing field 'Parent.second_surname'
        db.alter_column(u'signup_parent', 'second_surname', self.gf('django.db.models.fields.CharField')(default='', max_length=64))

        # Changing field 'Parent.state'
        db.alter_column(u'signup_parent', 'state', self.gf('django.db.models.fields.CharField')(default='', max_length=3))

        # Changing field 'Parent.second_name'
        db.alter_column(u'signup_parent', 'second_name', self.gf('django.db.models.fields.CharField')(default='', max_length=64))

        # Changing field 'Parent.occupation'
        db.alter_column(u'signup_parent', 'occupation', self.gf('django.db.models.fields.CharField')(default='', max_length=32))

    def backwards(self, orm):

        # Changing field 'Counselor.bus'
        db.alter_column(u'signup_counselor', 'bus', self.gf('django.db.models.fields.CharField')(max_length=16, null=True))

        # Changing field 'Counselor.badge_name'
        db.alter_column(u'signup_counselor', 'badge_name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'Counselor.structure'
        db.alter_column(u'signup_counselor', 'structure', self.gf('django.db.models.fields.CharField')(max_length=16, null=True))

        # Changing field 'Counselor.second_surname'
        db.alter_column(u'signup_counselor', 'second_surname', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'Counselor.second_name'
        db.alter_column(u'signup_counselor', 'second_name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'Counselor.cabin'
        db.alter_column(u'signup_counselor', 'cabin', self.gf('django.db.models.fields.CharField')(max_length=16, null=True))

        # Changing field 'Camper.second_surname'
        db.alter_column(u'signup_camper', 'second_surname', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'Camper.occupation'
        db.alter_column(u'signup_camper', 'occupation', self.gf('django.db.models.fields.CharField')(max_length=32, null=True))

        # Changing field 'Camper.state'
        db.alter_column(u'signup_camper', 'state', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))

        # Changing field 'Camper.passport'
        db.alter_column(u'signup_camper', 'passport', self.gf('django.db.models.fields.CharField')(max_length=16, null=True))

        # Changing field 'Camper.cabin'
        db.alter_column(u'signup_camper', 'cabin', self.gf('django.db.models.fields.CharField')(max_length=16, null=True))

        # Changing field 'Camper.province'
        db.alter_column(u'signup_camper', 'province', self.gf('django.db.models.fields.CharField')(max_length=32, null=True))

        # Changing field 'Camper.bus'
        db.alter_column(u'signup_camper', 'bus', self.gf('django.db.models.fields.CharField')(max_length=16, null=True))

        # Changing field 'Camper.badge_name'
        db.alter_column(u'signup_camper', 'badge_name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'Camper.structure'
        db.alter_column(u'signup_camper', 'structure', self.gf('django.db.models.fields.CharField')(max_length=16, null=True))

        # Changing field 'Camper.registrar'
        db.alter_column(u'signup_camper', 'registrar', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'Camper.second_name'
        db.alter_column(u'signup_camper', 'second_name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'Payment.notes'
        db.alter_column(u'signup_payment', 'notes', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'Guest.badge_name'
        db.alter_column(u'signup_guest', 'badge_name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'Guest.second_surname'
        db.alter_column(u'signup_guest', 'second_surname', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'Guest.second_name'
        db.alter_column(u'signup_guest', 'second_name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'Guest.cabin'
        db.alter_column(u'signup_guest', 'cabin', self.gf('django.db.models.fields.CharField')(max_length=16, null=True))

        # Changing field 'Parent.province'
        db.alter_column(u'signup_parent', 'province', self.gf('django.db.models.fields.CharField')(max_length=32, null=True))

        # Changing field 'Parent.second_surname'
        db.alter_column(u'signup_parent', 'second_surname', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'Parent.state'
        db.alter_column(u'signup_parent', 'state', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))

        # Changing field 'Parent.second_name'
        db.alter_column(u'signup_parent', 'second_name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'Parent.occupation'
        db.alter_column(u'signup_parent', 'occupation', self.gf('django.db.models.fields.CharField')(max_length=32, null=True))

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
            'docs_signed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'province': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'registrar': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
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
            'gov_id': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'second_surname': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'})
        },
        u'signup.payment': {
            'Meta': {'ordering': "['-payment_date']", 'object_name': 'Payment'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'payment_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'receipt_id': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['signup']