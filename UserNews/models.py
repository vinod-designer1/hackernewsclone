from django.db import models
from HackerNews.models import BaseModel
from django.contrib.auth.models import User
from NewsCollector.models import HackerNewsArticles
# Create your models here.
class UserNewsRelation(BaseModel):
  user = models.ForeignKey(User, related_name="user", blank=True, null=True)
  article = models.ForeignKey(HackerNewsArticles, blank=True, null=True, related_name="article")
  read = models.BooleanField('read', default=False)
  deleted = models.BooleanField('deleted', default=False)


  def __unicode__(self):
    return self.id
