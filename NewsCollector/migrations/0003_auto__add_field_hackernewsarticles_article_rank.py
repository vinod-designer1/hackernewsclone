# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'HackerNewsArticles.article_rank'
        db.add_column(u'NewsCollector_hackernewsarticles', 'article_rank',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=2147483646),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'HackerNewsArticles.article_rank'
        db.delete_column(u'NewsCollector_hackernewsarticles', 'article_rank')


    models = {
        u'NewsCollector.hackernewsarticles': {
            'Meta': {'object_name': 'HackerNewsArticles'},
            'article_comment_count': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'article_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'primary_key': 'True'}),
            'article_name': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'article_posted_by': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'article_posted_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 8, 1, 0, 0)', 'null': 'True', 'blank': 'True'}),
            'article_rank': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2147483646'}),
            'article_text': ('django.db.models.fields.TextField', [], {'max_length': '5000', 'null': 'True', 'blank': 'True'}),
            'article_upvotes': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'article_url': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['NewsCollector']