from django.http import HttpResponse, Http404
from datetime import datetime, timedelta
from django.shortcuts import render_to_response

def hello(request):
  return HttpResponse("Hello World!")

def current_datetime(request):
  current_date = str(datetime.now())
  return render_to_response('dateapp/current_datetime.html', locals())

def hours_ahead(request, offset):
  try:
    hour_offset = int(offset)
  except ValueError:
    raise Http404()
  next_time = datetime.now() + timedelta(hours=hour_offset)
  return render_to_response('dateapp/hours_ahead.html', locals())

def display_meta(request):
  values = request.META.items()
  values.sort()
  return render_to_response('dateapp/display_meta.html', locals())
