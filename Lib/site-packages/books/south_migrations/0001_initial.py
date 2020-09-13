# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Editor'
        db.create_table(u'books_editor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'books', ['Editor'])

        # Adding model 'Book'
        db.create_table(u'books_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('validated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('start_publication_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('end_publication_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('lang', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
            ('authors', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('editor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['books.Editor'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('affiliate_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('isbn_10', self.gf('django.db.models.fields.CharField')(max_length=10, unique=True, null=True, blank=True)),
            ('isbn_13', self.gf('django.db.models.fields.CharField')(max_length=13, unique=True, null=True, blank=True)),
            ('asin', self.gf('django.db.models.fields.CharField')(max_length=20, unique=True, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('cover', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'books', ['Book'])


    def backwards(self, orm):
        # Deleting model 'Editor'
        db.delete_table(u'books_editor')

        # Deleting model 'Book'
        db.delete_table(u'books_book')


    models = {
        u'books.book': {
            'Meta': {'object_name': 'Book'},
            'affiliate_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'asin': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'editor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['books.Editor']"}),
            'end_publication_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn_10': ('django.db.models.fields.CharField', [], {'max_length': '10', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'isbn_13': ('django.db.models.fields.CharField', [], {'max_length': '13', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'start_publication_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'validated': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'books.editor': {
            'Meta': {'object_name': 'Editor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['books']