from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from synnit.forms import SyntiForm
from synnit.lauriextra import taulukko_yksi_syntinen, aseta_cache_tarkistus
from synnit.models import TunnustettuSynti, Synnintekija

import numpy.random as npr
import os

def tarkista(tarkistus):
    tarkistus_cache = cache.get('tarkistusluku_cache')
    if(tarkistus_cache == tarkistus):
        tarkistus = 1
        return False
    else:
        return tarkistus

def SyntiAppi(request, tarkistus=0):
    
    # Tässä sivun salausta
    if(tarkista(tarkistus)):
        return HttpResponseRedirect(reverse('SyntiAppi', kwargs={'tarkistus': 0}))

    if request.method == 'POST':
        form = SyntiForm(request.POST, initial={'tekija': cache.get('tekija_cache')})
        
        if form.is_valid():
            form.save()
            
            tekija = get_object_or_404(Synnintekija, pk=form['tekija'].value())
            taulukko_yksi_syntinen(tekija)            

            tarkistus = aseta_cache_tarkistus(palauta=True)
            cache.set('tekija_cache', tekija)
            
            return HttpResponseRedirect(reverse('SyntiAppi', kwargs={'tarkistus': tarkistus}))
    else:
        form = SyntiForm()
    
    return render(request, 'synnit/syntiappi.html', {'form': form,
                                                     'nayta_kuva': tarkistus})

def Yhteenveto(request):
    return
     
