from django.http import HttpResponse, Http404
from datetime import datetime, timedelta

def hello(request):
  return HttpResponse("Hello World!")

def current_datetime(request):
  now = str(datetime.now())
  return HttpResponse("It is " + now)

def hours_ahead(request, offset):
  try:
    offset = int(offset)
  except ValueError:
    raise Http404()
  dt = datetime.now() + timedelta(hours=offset)
  assert False
  html = "In %s hour(s), it will be %s." % (offset, dt)
  return HttpResponse(html)
