from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from datetime import datetime
import threading
import Queue
import atexit

from ForkTube.forker.models import ForkItem, ForkItemForm

def root(request):

    if request.method == 'POST': # If the form has been submitted...

        # XXX: Validate
        password = request.POST['pass']
        username = request.POST['username']
        url = request.POST['url'] 

        if 'http://www.youtube.com/watch?v=' not in url or 'http://youtube.com/watch?v=' not in url:
            print "Skiddaddle"


        return HttpResponseRedirect('/forking') # Redirect after POST
    else:
        form = ForkItemForm() # An unbound form

    return render_to_response('root.html', context_instance=RequestContext(request))

def forking(request):
    return render_to_response('processing.html', context_instance=RequestContext(request))


#@postpone
def download(username, password, url):
    #DOWNLOAD THAT SHIT

    #XXX IF NOT FUCKED UPLOAD THAT SHIT
    upload(username, password, url)
    return

#@postpone
def upload(username, password, url):
    return

# Stolen from the internet
# XXX: FUCK THIS WHY IS THIS HERE JUST MAKE THIS CELERY INSTEAD
def _worker():
    while True:
        func, args, kwargs = _queue.get()
        try:
            func(*args, **kwargs)
        except:
            pass # bork or ignore here; ignore for now
        finally:
            _queue.task_done() # so we can join at exit

def postpone(func):
    def decorator(*args, **kwargs):
        _queue.put((func, args, kwargs))
        return decorator

    _queue = Queue.Queue()
    _thread = threading.Thread(target = _worker) # one is enough; it's postponed after all
    _thread.daemon = True # so we can exit
    _thread.start()

    def _cleanup():
        _queue.join() # so we don't exit too soon
        atexit.register(_cleanup)
