import urllib2
import httplib
import logging
import json
from utils.common import is_json


# Standard instance for logger with __name__
stdLogger = logging.getLogger(__name__)

def urlopener(url):
  """
  Fetches the give url and handles exceptions if any while fetching
  """
  try: 
    response = urllib2.urlopen(url)
  except urllib2.HTTPError, e:
    stdLogger.error('HTTPError = ' + str(e.code))
  except urllib2.URLError, e:
    stdLogger.error('URLError = ' + str(e.reason))
  except httplib.HTTPException, e:
    stdLogger.error('HTTPException')
  except Exception:
    import traceback
    stdLogger.error('generic exception: ' + traceback.format_exc())

  return response

class HackerNewsFetcher():

  def __init__(self, n):
    self.n = int(n)
  
  def get_item_details(self, item_id):
    """
    In hackernews Stories, comments, jobs, Ask HNs and even polls are just items. 
    They're identified by their ids, which are unique integers, 
    and can be fetched using https://hacker-news.firebaseio.com/v0/item/<item_id>.json?print=pretty.
    """
    stdLogger.debug('Started Getting Item Details for id %s', item_id)

    url = "https://hacker-news.firebaseio.com/v0/item/%s.json?print=pretty" % (str(item_id),)
    response = urlopener(url)
    item_details = {}

    if response:
      data = response.read()
      if is_json(data):
        item_details = json.loads(data)

    print item_details

    return item_details

  def get_n_topstory_ids(self):
    """
    This method returns ids of top n stories in hackernews
    we can fetch them from 
    https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty
    """
    stdLogger.debug('Started Getting all top story ids')

    url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
    response = urlopener(url)
    list_of_top_story_ids = []

    if response:
      data = response.read()
      if is_json(data):
        list_of_top_story_ids = json.loads(data)

    # if len(list_of_top_story_ids) > self.n:
    #   list_of_top_story_ids = list_of_top_story_ids[:self.n]

    # print list_of_top_story_ids

    return list_of_top_story_ids

  def get_n_topstory_details(self):
    """
    This method returns list of to n top stories in hackernews along with following details
    id, posted_by, url, upvotes, comments, title, posted_on(time)
    """
    stdLogger.debug('Started Getting all top story details')

    no_of_stories_added = 0

    # Get n top story ids
    ids_of_top_n_stories = self.get_n_topstory_ids()

    top_n_story_details = []

    # iterate over ids and get story details for each
    for story_id in ids_of_top_n_stories:
      story_details = self.get_item_details(story_id)

      if story_details:
        if story_details['type'] == 'story':
          top_n_story_details.append(story_details)
          no_of_stories_added += 1

      if no_of_stories_added == self.n:
        break

    return top_n_story_details