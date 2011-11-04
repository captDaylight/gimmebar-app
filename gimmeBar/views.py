from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from app.models import *
import json, urllib

def landing(request):
	return render_to_response('app/index.html',context_instance=RequestContext(request))