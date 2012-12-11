from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from main.forms import MessageForm
from main.models import Message

def index(request):
    visits = Message.objects.all()
    data = {
        'visits': visits
    }

    return render_to_response("index.html", data, context_instance=RequestContext(request))

def agregar(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MessageForm()

    data = {
        'form': form,
    }

    return render_to_response("add.html", data, context_instance=RequestContext(request))

def editar(request, id):
    message = get_object_or_404(Message, pk=id)
    if request.method == "POST":
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MessageForm(instance=message)

    data = {
        'form': form
    }
    return render_to_response("edit.html", data, context_instance=RequestContext(request))

def eliminar(request, id):
    #Podriamos solicitar confirmacion antes de proceder...
    message = get_object_or_404(Message, pk=id) #instancia
    message.delete()
    return HttpResponseRedirect('/')
