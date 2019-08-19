from .forms import SyntiForm
from .lauriextra import lisaa_nimet_maarat 
from .models import Synnintekija, TunnustettuSynti  
from django.core.cache import cache 
from django.shortcuts import render
from django.views.generic.edit import FormView 


class Syntiappi(FormView):
    form_class = SyntiForm 
    success_url = 'kuvalla/'
    template_name = 'synnit/syntiappi.html'
    
    def form_valid(self, form):
        form.save()
        
        tekija_id = form['tekija'].value()
        tekija = Synnintekija.objects.get(pk=tekija_id)
        cache.set('edellinen_tekija', tekija)

        context = super().get_context_data()
        context = lisaa_nimet_maarat(context, tekija, TunnustettuSynti)

        return render(self.request, 'synnit/syntiappi_kuvalla.html', context)
    
    def get_initial(self):
        tekija = cache.get('edellinen_tekija')
        cache.delete('edellinen_tekija')
        return {'tekija': tekija}


class SyntiappiKuvalla(Syntiappi):
    success_url = '/kuvalla'
    template_name = 'synnit/syntiappi_kuvalla.html'
    





