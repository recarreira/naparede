# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Painting'
        db.create_table(u'painting_painting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('Description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'painting', ['Painting'])


    def backwards(self, orm):
        # Deleting model 'Painting'
        db.delete_table(u'painting_painting')


    models = {
        u'painting.painting': {
            'Description': ('django.db.models.fields.TextField', [], {}),
            'Meta': {'object_name': 'Painting'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['painting']