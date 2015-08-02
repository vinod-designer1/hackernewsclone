from .models import UserNewsRelation
from NewsCollector.utils import get_articles
import datetime

# @TODO imporve fetching articles as articles from last update will not change any user requested in mean time
#   should get the articles from cache reduces db requests
#   and every user related articles should be fetched more efficiently
def get_user_articles(limit, user):
  """
  Fetches articles and structure article data
  it check if user logged in if yes it get whether user read or delete the article
  """
  articles = get_articles(limit)
  articles_with_user_data = []

  for article in articles:
    article_info = {}
    article_info['id'] = article.article_id
    article_info['name'] = article.article_name
    article_info['postedon'] = article.article_posted_on.strftime('%m/%d/%Y %H:%M:%S')
    article_info['postedby'] = article.article_posted_by
    article_info['comments'] = article.article_comment_count
    article_info['url'] = article.article_url
    article_info['text'] = article.article_text
    article_info['upvotes'] = article.article_upvotes
    article_info['read'] = False


    if user.is_authenticated():
      try:
        usernews_rel = UserNewsRelation.objects.get(user=user, article=article)
      except UserNewsRelation.DoesNotExist:
        usernews_rel = None

      if usernews_rel:
        article_info['read'] = usernews_rel.read
        if not usernews_rel.deleted:
          articles_with_user_data.append(article_info)
      else:
        articles_with_user_data.append(article_info)
    else:
      articles_with_user_data.append(article_info)

  # sorts articles based on timestamp posted on the latest posted article is showed on top
  articles_with_user_data.sort(
    key=lambda x: (datetime.datetime.strptime(x['postedon'], '%m/%d/%Y %H:%M:%S') - datetime.datetime(1970,1,1, tzinfo=None)),
    reverse=True)
  return articles_with_user_data