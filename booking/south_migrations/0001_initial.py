# flake8: noqa
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BookingStatus'
        db.create_table(u'booking_bookingstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'booking', ['BookingStatus'])

        # Adding model 'BookingStatusTranslation'
        db.create_table(u'booking_bookingstatustranslation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['booking.BookingStatus'])),
        ))
        db.send_create_signal(u'booking', ['BookingStatusTranslation'])

        # Adding model 'Booking'
        db.create_table(u'booking_booking', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='bookings', null=True, to=orm['auth.User'])),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sessions.Session'], null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('forename', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('nationality', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('street1', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('street2', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('special_request', self.gf('django.db.models.fields.TextField')(max_length=1024, blank=True)),
            ('date_from', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('date_until', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('booking_id', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('booking_status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['booking.BookingStatus'])),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=1024, blank=True)),
        ))
        db.send_create_signal(u'booking', ['Booking'])

        # Adding model 'BookingItem'
        db.create_table(u'booking_bookingitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quantity', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('persons', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('booking', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['booking.Booking'])),
        ))
        db.send_create_signal(u'booking', ['BookingItem'])

        # Adding model 'ExtraPersonInfo'
        db.create_table(u'booking_extrapersoninfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('forename', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('arrival', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('booking', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['booking.Booking'])),
            ('message', self.gf('django.db.models.fields.TextField')(max_length=1024, blank=True)),
        ))
        db.send_create_signal(u'booking', ['ExtraPersonInfo'])


    def backwards(self, orm):
        # Deleting model 'BookingStatus'
        db.delete_table(u'booking_bookingstatus')

        # Deleting model 'BookingStatusTranslation'
        db.delete_table(u'booking_bookingstatustranslation')

        # Deleting model 'Booking'
        db.delete_table(u'booking_booking')

        # Deleting model 'BookingItem'
        db.delete_table(u'booking_bookingitem')

        # Deleting model 'ExtraPersonInfo'
        db.delete_table(u'booking_extrapersoninfo')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'booking.booking': {
            'Meta': {'ordering': "['-creation_date']", 'object_name': 'Booking'},
            'booking_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'booking_status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['booking.BookingStatus']"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_from': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_until': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'forename': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sessions.Session']", 'null': 'True', 'blank': 'True'}),
            'special_request': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'blank': 'True'}),
            'street1': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'street2': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'bookings'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'booking.bookingitem': {
            'Meta': {'ordering': "['-booking__creation_date']", 'object_name': 'BookingItem'},
            'booking': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['booking.Booking']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'persons': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        u'booking.bookingstatus': {
            'Meta': {'object_name': 'BookingStatus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'booking.bookingstatustranslation': {
            'Meta': {'object_name': 'BookingStatusTranslation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['booking.BookingStatus']"})
        },
        u'booking.extrapersoninfo': {
            'Meta': {'ordering': "['-booking__creation_date']", 'object_name': 'ExtraPersonInfo'},
            'arrival': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'booking': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['booking.Booking']"}),
            'forename': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sessions.session': {
            'Meta': {'object_name': 'Session', 'db_table': "'django_session'"},
            'expire_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'session_data': ('django.db.models.fields.TextField', [], {}),
            'session_key': ('django.db.models.fields.CharField', [], {'max_length': '40', 'primary_key': 'True'})
        }
    }

    complete_apps = ['booking']
