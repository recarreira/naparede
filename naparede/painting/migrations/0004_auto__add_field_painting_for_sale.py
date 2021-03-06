# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Painting.for_sale'
        db.add_column(u'painting_painting', 'for_sale',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Painting.for_sale'
        db.delete_column(u'painting_painting', 'for_sale')


    models = {
        u'author.author': {
            'Meta': {'object_name': 'Author'},
            'about': ('django.db.models.fields.TextField', [], {'default': "'about'"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'name'", 'max_length': '200'})
        },
        u'painting.galery': {
            'Meta': {'object_name': 'Galery'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'painting.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'painting': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'image_painting'", 'to': u"orm['painting.Painting']"})
        },
        u'painting.painting': {
            'Meta': {'object_name': 'Painting'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'painting_author'", 'to': u"orm['author.Author']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "'description'"}),
            'for_sale': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'galery': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['painting.Galery']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'title'", 'max_length': '200'})
        }
    }

    complete_apps = ['painting']