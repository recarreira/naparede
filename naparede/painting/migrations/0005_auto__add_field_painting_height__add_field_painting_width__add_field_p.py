# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Painting.height'
        db.add_column(u'painting_painting', 'height',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Painting.width'
        db.add_column(u'painting_painting', 'width',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Painting.technique'
        db.add_column(u'painting_painting', 'technique',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Painting.price'
        db.add_column(u'painting_painting', 'price',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Painting.discount'
        db.add_column(u'painting_painting', 'discount',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Painting.height'
        db.delete_column(u'painting_painting', 'height')

        # Deleting field 'Painting.width'
        db.delete_column(u'painting_painting', 'width')

        # Deleting field 'Painting.technique'
        db.delete_column(u'painting_painting', 'technique')

        # Deleting field 'Painting.price'
        db.delete_column(u'painting_painting', 'price')

        # Deleting field 'Painting.discount'
        db.delete_column(u'painting_painting', 'discount')


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
            'description': ('django.db.models.fields.TextField', [], {}),
            'discount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'for_sale': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'galery': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['painting.Galery']", 'symmetrical': 'False'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'technique': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['painting']