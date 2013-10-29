# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Galery'
        db.create_table(u'painting_galery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'painting', ['Galery'])

        # Adding field 'Painting.author'
        db.add_column(u'painting_painting', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='painting_author', to=orm['author.Author']),
                      keep_default=False)

        # Adding M2M table for field Galery on 'Painting'
        m2m_table_name = db.shorten_name(u'painting_painting_Galery')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('painting', models.ForeignKey(orm[u'painting.painting'], null=False)),
            ('galery', models.ForeignKey(orm[u'painting.galery'], null=False))
        ))
        db.create_unique(m2m_table_name, ['painting_id', 'galery_id'])


    def backwards(self, orm):
        # Deleting model 'Galery'
        db.delete_table(u'painting_galery')

        # Deleting field 'Painting.author'
        db.delete_column(u'painting_painting', 'author_id')

        # Removing M2M table for field Galery on 'Painting'
        db.delete_table(db.shorten_name(u'painting_painting_Galery'))


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
            'Galery': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['painting.Galery']", 'symmetrical': 'False'}),
            'Meta': {'object_name': 'Painting'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'painting_author'", 'to': u"orm['author.Author']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "'description'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'title'", 'max_length': '200'})
        }
    }

    complete_apps = ['painting']