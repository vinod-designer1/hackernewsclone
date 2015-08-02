from .models import HackerNewsArticles

def get_articles(limit):
  articles = HackerNewsArticles.objects.order_by("-modified_date", "article_rank")[:limit]
  return articles