from django.core.management.base import BaseCommand, CommandError
from NewsCollector.models import HackerNewsArticles
from NewsCollector.newsfetchapi import HackerNewsFetcher
import datetime
import logging
import pytz

# Standard instance for logger with __name__
stdLogger = logging.getLogger(__name__)

# @TODO need to fix datetime for article
class Command(BaseCommand):
  help = 'fetch articles from hackernews'

  def add_arguments(self, parser):
    parser.add_argument('no_of_articles', type=int)

  def handle(self, *args, **options):

    no_of_articles = args[0]

    self.stdout.write(no_of_articles)
    
    try:
      # Extract Articles 
      top_n_articles = HackerNewsFetcher(no_of_articles).get_n_topstory_details()
    except Exception:
      import traceback
      raise CommandError('Error While Getting articles %s', traceback.format_exc())

    self.stdout.write('Extracted Articles')

    # Insert articles in to db
    for article in top_n_articles:
      newsarticle, created = HackerNewsArticles.objects.get_or_create(article_id=article['id'])

      if created:
        newsarticle.article_name = article['title']

        if 'url' in article:
          newsarticle.article_url = article['url']

        if 'text' in article:
          newsarticle.article_text = article['text']

        newsarticle.article_posted_by = article['by']
        newsarticle.article_posted_on = datetime.datetime.fromtimestamp(int(article['time']))
      
      newsarticle.article_comment_count = article['descendants']
      newsarticle.article_upvotes = article['score']

      newsarticle.save()




