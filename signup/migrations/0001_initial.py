# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Payment'
        db.create_table(u'signup_payment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('receipt_id', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('payment_date', self.gf('django.db.models.fields.DateField')()),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'signup', ['Payment'])

        # Adding model 'Parent'
        db.create_table(u'signup_parent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('second_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('first_surname', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('second_surname', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('birth_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('province', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('gov_id', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'signup', ['Parent'])

        # Adding model 'Camper'
        db.create_table(u'signup_camper', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('second_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('first_surname', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('second_surname', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('birth_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('province', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('balance', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=5, decimal_places=2)),
            ('no_pay', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('badge_name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('passport', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('birth_cert_num', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('birth_cert_fol', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('birth_cert_book', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('registrar', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('docs_signed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mother', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='mothered', null=True, to=orm['signup.Parent'])),
            ('father', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='fathered', null=True, to=orm['signup.Parent'])),
            ('special_case', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('assigned_counselor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['signup.Counselor'], null=True, blank=True)),
        ))
        db.send_create_signal(u'signup', ['Camper'])

        # Adding model 'Counselor'
        db.create_table(u'signup_counselor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('second_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('first_surname', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('second_surname', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('balance', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=5, decimal_places=2)),
            ('no_pay', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('badge_name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('small_group', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['logistics.SmallGroup'], unique=True)),
        ))
        db.send_create_signal(u'signup', ['Counselor'])


    def backwards(self, orm):
        # Deleting model 'Payment'
        db.delete_table(u'signup_payment')

        # Deleting model 'Parent'
        db.delete_table(u'signup_parent')

        # Deleting model 'Camper'
        db.delete_table(u'signup_camper')

        # Deleting model 'Counselor'
        db.delete_table(u'signup_counselor')


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
        u'logistics.smallgroup': {
            'Meta': {'ordering': "['title']", 'object_name': 'SmallGroup'},
            'bus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['logistics.Bus']", 'null': 'True', 'blank': 'True'}),
            'cabin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['logistics.Cabin']", 'null': 'True', 'blank': 'True'}),
            'generation': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'signup.camper': {
            'Meta': {'ordering': "['first_surname']", 'object_name': 'Camper'},
            'assigned_counselor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['signup.Counselor']", 'null': 'True', 'blank': 'True'}),
            'badge_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'birth_cert_book': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'birth_cert_fol': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'birth_cert_num': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'birth_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
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
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'first_surname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_pay': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'second_surname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'small_group': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['logistics.SmallGroup']", 'unique': 'True'})
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