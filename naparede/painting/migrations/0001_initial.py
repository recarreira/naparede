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
            ('title', self.gf('django.db.models.fields.CharField')(default='title', max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(default='description')),
        ))
        db.send_create_signal(u'painting', ['Painting'])

        # Adding model 'Image'
        db.create_table(u'painting_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('painting', self.gf('django.db.models.fields.related.ForeignKey')(related_name='image_painting', to=orm['painting.Painting'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'painting', ['Image'])


    def backwards(self, orm):
        # Deleting model 'Painting'
        db.delete_table(u'painting_painting')

        # Deleting model 'Image'
        db.delete_table(u'painting_image')


    models = {
        u'painting.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'painting': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'image_painting'", 'to': u"orm['painting.Painting']"})
        },
        u'painting.painting': {
            'Meta': {'object_name': 'Painting'},
            'description': ('django.db.models.fields.TextField', [], {'default': "'description'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'title'", 'max_length': '200'})
        }
    }

    complete_apps = ['painting']