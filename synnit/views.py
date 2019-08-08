from django.core.cache import cache
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from synnit.forms import SyntiForm
from synnit.lauriextra import taulukko_yksi_syntinen, aseta_cache_tarkistus
from synnit.models import TunnustettuSynti, Synnintekija

import numpy.random as npr
import os

def tarkista(tarkistus):
    
    if(cache.get('tarkistusluku_cache') == tarkistus):
        return True, False
    
    elif(tarkistus == 1):
        cache.delete('tekija_cache')
        aseta_cache_tarkistus()
        return False, False
    
    return False, True

def SyntiAppi(request, tarkistus=1):

    # Tässä sivun salausta ja näyttää vai ei näyttää kuva
    nayta_kuva, laukaise404 = tarkista(tarkistus)
    if(laukaise404):
        raise Http404()

    if request.method == 'POST':
        form = SyntiForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            tekija = get_object_or_404(Synnintekija, pk=form['tekija'].value())
            
            if not taulukko_yksi_syntinen(tekija):
                tarkistus = 1
            else:
                tarkistus = aseta_cache_tarkistus(palauta=True)
            
            cache.set('tekija_cache', tekija)
            
            return HttpResponseRedirect(reverse('SyntiAppi', kwargs={'tarkistus': tarkistus}))
    else:
        form = SyntiForm(initial={'tekija': cache.get('tekija_cache')})
    
    return render(request, 'synnit/syntiappi.html', {'form': form,
                                                     'nayta_kuva': nayta_kuva})

def Yhteenveto(request):
    return
     
