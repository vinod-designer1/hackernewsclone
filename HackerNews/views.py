from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest,HttpResponseNotFound
import json
from utils.common import is_json
from django.contrib.auth import logout
from NewsCollector.models import HackerNewsArticles
from UserNews.models import UserNewsRelation
from utils.common import is_json
from django.core import serializers
import datetime
import pytz

# Create your views here.
def homepage_view(request):
  return render(request, 'index.html')


def login_view(request):
  if not is_json(request.body):
    return HttpResponseBadRequest(json.dumps({'error': 'not valid data'}), mimetype="application/json")

  data = json.loads(request.body)
  username = ''
  password = ''

  if 'username' in data:
    username = data['username']

  if 'password' in data:
    password = data['password']

  if username.strip() == '' or password.strip() == '':
    return HttpResponseBadRequest(json.dumps({'error': 'invalid username or password'}), mimetype="application/json")

  print 'login', username, password


  user = authenticate(username=username, password=password)
  if user is not None:
    if user.is_active:
      login(request, user)
      return HttpResponse(json.dumps({'message': 'login successful'}), mimetype="application/json")
    else:
      return HttpResponseBadRequest(json.dumps({'error': 'account blocked!'}), mimetype="application/json")
  else:
    return HttpResponseBadRequest(json.dumps({'error': 'invalid login'}), mimetype="application/json")





def register_view(request):
  if not is_json(request.body):
    return HttpResponseBadRequest(json.dumps({'error': 'not valid data'}), mimetype="application/json")

  data = json.loads(request.body)
  username = ''
  password = ''

  if 'username' in data:
    username = data['username']

  if 'password' in data:
    password = data['password']

  if username.strip() == '' or password.strip() == '':
    return HttpResponseBadRequest(json.dumps({'error': 'invalid username or password'}), mimetype="application/json")

  try:
    user = User.objects.get(username=username)
  except User.DoesNotExist:
    user = None

  if user is None:
    user = User.objects.create_user(username, '', password)
    return HttpResponse(json.dumps({'message': 'success'}), mimetype="application/json")
  else:
    return HttpResponseBadRequest(json.dumps({'error': 'please choose another username'}), mimetype="application/json")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

# @TODO imporve fetching articles as articles from last update will not change any user requested in mean time
#   should get the articles from cache reduces db requests
#   and every user related articles should be fetched more efficiently
def get_user_articles(request):
  articles = get_articles(request)
  articles_with_user_data = []

  for article in articles:
    article_info = {}
    article_info['id'] = article.article_id
    article_info['name'] = article.article_name
    article_info['postedon'] = article.article_posted_on.strftime('%m/%d/%Y %H:%M:%S')
    article_info['postedby'] = article.article_posted_by
    article_info['comments'] = article.article_comment_count
    article_info['url'] = article.article_url
    article_info['upvotes'] = article.article_upvotes
    article_info['read'] = False


    if request.user.is_authenticated():
      try:
        usernews_rel = UserNewsRelation.objects.get(user=request.user, article=article)
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

  articles_with_user_data.sort(
    key=lambda x: (datetime.datetime.strptime(x['postedon'], '%m/%d/%Y %H:%M:%S') - datetime.datetime(1970,1,1, tzinfo=None)),
    reverse=True)
  return articles_with_user_data

def get_articles(request):
  articles = HackerNewsArticles.objects.order_by("modified_date")[:90]
  return articles

# Create your views here.
def get_articles_view(request):
  articles = get_user_articles(request)

  return HttpResponse(json.dumps(articles), mimetype="application/json")


    

  
