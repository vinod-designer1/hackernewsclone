from django.shortcuts import render
from NewsCollector.models import HackerNewsArticles
from UserNews.models import UserNewsRelation
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest,HttpResponseNotFound
from utils.common import is_json
import json


def mark_article_read_or_delete_view(request):
  """
  Endpoint view:
  help to mark article read, unread or delete for a particular user
  """
  if request.user.is_authenticated():
    if not is_json(request.body):
      return HttpResponseBadRequest(json.dumps({'error': 'not valid data'}), mimetype="application/json")

    data = json.loads(request.body)
    read = False
    delete = False
    article = None
    userarticle = None

    if 'article_id' in data:
      article_id = data['article_id']
      try:
        article = HackerNewsArticles.objects.get(article_id=article_id)
      except HackerNewsArticles.DoesNotExist:
        article = None

    if article is None:
      return HttpResponseBadRequest(json.dumps({'error': 'need to specify article!'}), mimetype="application/json")

    if 'read' in data:
      read = data['read']
    elif 'remove' in data:
      delete = data['remove']
    else:
      return HttpResponseBadRequest(json.dumps({'error': 'should specify what action!'}), mimetype="application/json")
    
    userarticle, created = UserNewsRelation.objects.get_or_create(user=request.user, article=article)

    if read:
      userarticle.read = not userarticle.read

    if delete:
      userarticle.deleted = not userarticle.deleted

    userarticle.save()

    return HttpResponse(json.dumps({'message': 'Marked Succesfully!'}), mimetype="application/json")
  else:
    return HttpResponseBadRequest(json.dumps({'error': 'user should login!'}), mimetype="application/json")