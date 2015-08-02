from django.test import Client, TestCase
from NewsCollector.newsfetchapi import HackerNewsFetcher
import json
import datetime
from django.core import management

class UserStoryTest(TestCase):
  def test_if_story_order_is_correct_user_not_logged_in(self):
    no_of_articles = 10
    client = Client()

    top_n_articles = HackerNewsFetcher(no_of_articles).get_n_topstory_details()

    top_n_articles.sort(
    key=lambda x: (datetime.datetime.fromtimestamp(int(x['time'])) - datetime.datetime(1970,1,1, tzinfo=None)),
    reverse=True)

    management.call_command('fetcharticles', str(no_of_articles))

    resp = client.get('/getarticles/?limit='+str(no_of_articles))
    self.assertEqual(resp.status_code, 200)

    articles = json.loads(resp.content)

    for i in range(0, no_of_articles):
      self.assertEqual(int(articles[i]['id']), int(top_n_articles[i]['id']))






