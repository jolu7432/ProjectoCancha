from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))
