# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Counselor.generation'
        db.add_column(u'signup_counselor', 'generation',
                      self.gf('django.db.models.fields.PositiveIntegerField')(max_length=1, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Counselor.structure'
        db.add_column(u'signup_counselor', 'structure',
                      self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Counselor.bus'
        db.add_column(u'signup_counselor', 'bus',
                      self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Counselor.second_name'
        db.alter_column(u'signup_counselor', 'second_name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'Counselor.cabin'
        db.alter_column(u'signup_counselor', 'cabin', self.gf('django.db.models.fields.CharField')(max_length=16, null=True))
        # Adding field 'Camper.generation'
        db.add_column(u'signup_camper', 'generation',
                      self.gf('django.db.models.fields.PositiveIntegerField')(max_length=1, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Camper.structure'
        db.add_column(u'signup_camper', 'structure',
                      self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Camper.bus'
        db.add_column(u'signup_camper', 'bus',
                      self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Camper.small_group'
        db.add_column(u'signup_camper', 'small_group',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['logistics.SmallGroup'], null=True, blank=True),
                      keep_default=False)


        # Changing field 'Camper.cabin'
        db.alter_column(u'signup_camper', 'cabin', self.gf('django.db.models.fields.CharField')(max_length=16, null=True))

        # Changing field 'Camper.second_name'
        db.alter_column(u'signup_camper', 'second_name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'Guest.second_name'
        db.alter_column(u'signup_guest', 'second_name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'Guest.cabin'
        db.alter_column(u'signup_guest', 'cabin', self.gf('django.db.models.fields.CharField')(max_length=6, null=True))

        # Changing field 'Payment.payment_date'
        db.alter_column(u'signup_payment', 'payment_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Parent.second_name'
        db.alter_column(u'signup_parent', 'second_name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

    def backwards(self, orm):
        # Deleting field 'Counselor.generation'
        db.delete_column(u'signup_counselor', 'generation')

        # Deleting field 'Counselor.structure'
        db.delete_column(u'signup_counselor', 'structure')

        # Deleting field 'Counselor.bus'
        db.delete_column(u'signup_counselor', 'bus')


        # User chose to not deal with backwards NULL issues for 'Counselor.second_name'
        raise RuntimeError("Cannot reverse this migration. 'Counselor.second_name' and its values cannot be restored.")

        # Changing field 'Counselor.cabin'
        db.alter_column(u'signup_counselor', 'cabin', self.gf('django.db.models.fields.CharField')(max_length=32, null=True))
        # Deleting field 'Camper.generation'
        db.delete_column(u'signup_camper', 'generation')

        # Deleting field 'Camper.structure'
        db.delete_column(u'signup_camper', 'structure')

        # Deleting field 'Camper.bus'
        db.delete_column(u'signup_camper', 'bus')

        # Deleting field 'Camper.small_group'
        db.delete_column(u'signup_camper', 'small_group_id')


        # Changing field 'Camper.cabin'
        db.alter_column(u'signup_camper', 'cabin', self.gf('django.db.models.fields.CharField')(max_length=32, null=True))

        # User chose to not deal with backwards NULL issues for 'Camper.second_name'
        raise RuntimeError("Cannot reverse this migration. 'Camper.second_name' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Guest.second_name'
        raise RuntimeError("Cannot reverse this migration. 'Guest.second_name' and its values cannot be restored.")

        # Changing field 'Guest.cabin'
        db.alter_column(u'signup_guest', 'cabin', self.gf('django.db.models.fields.CharField')(max_length=32, null=True))

        # Changing field 'Payment.payment_date'
        db.alter_column(u'signup_payment', 'payment_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 5, 31, 0, 0)))

        # User chose to not deal with backwards NULL issues for 'Parent.second_name'
        raise RuntimeError("Cannot reverse this migration. 'Parent.second_name' and its values cannot be restored.")

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
            'bus': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'cabin': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'generation': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'structure': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
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
            'bus': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'cabin': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'counselor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['signup.Counselor']"}),
            'docs_signed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'father': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fathered'", 'null': 'True', 'to': u"orm['signup.Parent']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'first_surname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'generation': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mother': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mothered'", 'null': 'True', 'to': u"orm['signup.Parent']"}),
            'no_pay': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'passport': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'registrar': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'second_surname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'small_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['logistics.SmallGroup']", 'null': 'True', 'blank': 'True'}),
            'special_case': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'structure': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'})
        },
        u'signup.counselor': {
            'Meta': {'ordering': "['first_surname']", 'object_name': 'Counselor'},
            'badge_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'bus': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'cabin': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'first_surname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'generation': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_pay': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'second_surname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'small_group': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['logistics.SmallGroup']", 'unique': 'True'}),
            'structure': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'})
        },
        u'signup.guest': {
            'Meta': {'ordering': "['first_surname']", 'object_name': 'Guest'},
            'badge_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'cabin': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'first_surname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_pay': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
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
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
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
            'payment_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'receipt_id': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['signup']