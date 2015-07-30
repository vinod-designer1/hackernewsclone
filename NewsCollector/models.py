from django.db import models
import datetime

# Create your models here.
class HackerNewsArticles(models.Model):
  article_id = models.CharField(unique=True, primary_key=True, max_length=255)
  article_name = models.CharField('Name', max_length=1000, blank=True, null=True)
  article_comment_count = models.CharField('CommentCount', max_length=500, blank=True, null=True)
  article_upvotes = models.CharField('Upvotes', max_length=500, blank=True, null=True)
  article_url = models.CharField('Url', max_length=500, blank=True, null=True)
  article_posted_on = models.DateTimeField('Date', default=datetime.datetime.now(), blank=True, null=True)
  article_posted_by = models.CharField('Postedby', max_length=500, blank=True, null=True)

  def __unicode__(self):
    return self.article_name