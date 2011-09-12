from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from datetime import datetime
import hashlib

from ForkTube.forker.models import ForkItem, ForkItemForm

def root(request):

    if request.method == 'POST': # If the form has been submitted...

        # XXX: Validate
        password = request.POST['password']
        username = request.POST['user']
        url = request.POST['url'] 

        form = ForkItemForm(request.POST)
        form.hashish= hashlib.sha1(password+username+url+str(datetime.now())).hexdigest()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/forking/' + form.hashish) # Redirect after POST

    else:
        form = ForkItemForm() # An unbound form

    return render_to_response('root.html', {'form': form}, context_instance=RequestContext(request))

def forking(request, hash):
    return render_to_response('processing.html', context_instance=RequestContext(request))


#@postpone
def download(hashish):


    upload(hashish)
    return

def upload(hashish):
    return
