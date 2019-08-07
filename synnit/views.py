from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from synnit.forms import SyntiForm
from synnit.lauriextra import taulukko_yksi_syntinen
from synnit.models import TunnustettuSynti, Synnintekija

import numpy.random as npr
import os

glo = npr.randint(1, 10000000000)

def SyntiAppi(request, luku=0):

    global glo

    if(glo == luku):
        luku = 1
    elif(luku != 0):
        glo = npr.randint(1, 10000000000)
        return HttpResponseNotFound('<h1>Sivua ei löytynyt</h1>')

    if request.method == 'POST':
        form = SyntiForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            tekija_id = form['tekija'].value()
            tekija = get_object_or_404(Synnintekija, pk=tekija_id)
            taulukko_yksi_syntinen(tekija)            

            glo = npr.randint(1, 10000000000)
            
            return HttpResponseRedirect(reverse('SyntiAppi', kwargs={'luku': glo}))
    else:
        form = SyntiForm()
    
    return render(request, 'synnit/syntiappi.html', {'form': form,
                                                     'nayta_kuva': luku})

def Yhteenveto(request):
    return
     
