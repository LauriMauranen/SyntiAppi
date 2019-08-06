from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from synnit.models import Synnintekija, Syntilaatu, TunnustettuSynti

from .forms import SyntiForm

def SyntiAppi(request):
    
    if request.method == 'POST':
        form = SyntiForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
    else:
        form = SyntiForm()
    
    return render(request, 'synnit/index.html', {'form': form})
     
