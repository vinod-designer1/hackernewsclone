# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HackerNewsArticles'
        db.create_table(u'NewsCollector_hackernewsarticles', (
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('article_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, primary_key=True)),
            ('article_name', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('article_comment_count', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('article_upvotes', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('article_url', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('article_posted_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 7, 31, 0, 0), null=True, blank=True)),
            ('article_posted_by', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
        ))
        db.send_create_signal(u'NewsCollector', ['HackerNewsArticles'])


    def backwards(self, orm):
        # Deleting model 'HackerNewsArticles'
        db.delete_table(u'NewsCollector_hackernewsarticles')


    models = {
        u'NewsCollector.hackernewsarticles': {
            'Meta': {'object_name': 'HackerNewsArticles'},
            'article_comment_count': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'article_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'primary_key': 'True'}),
            'article_name': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'article_posted_by': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'article_posted_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 7, 31, 0, 0)', 'null': 'True', 'blank': 'True'}),
            'article_upvotes': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'article_url': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['NewsCollector']