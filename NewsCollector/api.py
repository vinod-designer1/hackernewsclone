from tastypie.resources import ModelResource
from NewsCollector.models import HackerNewsArticles

class HackerNewsArticleResource(ModelResource):
  class Meta:
    queryset = HackerNewsArticles.objects.all()
    resource_name = 'newsarticles'