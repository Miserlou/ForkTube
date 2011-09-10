from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from datetime import datetime

from ForkTube.forker.models import ForkItem, ForkItemForm

def root(request):
    form = ForkItemForm()
    return render_to_response('root.html', {'form': form }, context_instance=RequestContext(request)) 
