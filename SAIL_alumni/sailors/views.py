from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Sailor

def sailors(request):
    all_sailors = Sailor.objects.all().values()
    template = loader.get_template('all_sailors.html')
    context = {
        'all_sailors': all_sailors,
    }
    return HttpResponse(template.render(context, request))
