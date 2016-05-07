from django.core.mail import EmailMessage
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

@csrf_exempt
def sendEmail(request):
    try:
        email = EmailMessage(request.POST['asunto'] + " Email: " + request.POST['email'],
                            "Solicitud de Contacto de parte de "+ request.POST['nombre'] + " para el complejo " + request.POST['complejo']
                            + " Mensaje: " + request.POST['mensaje'],
                            to=['canchaltoque@gmail.com'])
        email.send()
        return render_to_response('index.html', context_instance=RequestContext(request))
    except:
        return render_to_response('blog.html', context_instance=RequestContext(request))

@csrf_exempt
def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))

@csrf_exempt
def gestion(request):
    return render_to_response('gestion.html', context_instance=RequestContext(request))