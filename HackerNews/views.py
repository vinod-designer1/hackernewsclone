from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest,HttpResponseNotFound
import json
from utils.common import is_json

# Create your views here.
def homepage(request):
  return render(request, 'index.html')

def register(request):
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




    

  
