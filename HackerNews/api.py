from tastypie.api import Api

api = Api(api_name="v1")

from NewsCollector.api import HackerNewsArticleResource
api.register(HackerNewsArticleResource())