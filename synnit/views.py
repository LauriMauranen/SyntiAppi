from .forms import SyntiForm
from .lauriextra import lisaa_nimet_maarat
from .models import Synnintekija, TunnustettuSynti  
from django.core.cache import cache 
from django.shortcuts import render
from django.views.generic.edit import FormView 


class Syntiappi(FormView):
    form_class = SyntiForm 
    template_name = 'synnit/syntiappi_kuvalla.html'
    
    def form_valid(self, form):
        form.save()
        tekija_id = form['tekija'].value()
        context = super().get_context_data()
        context = lisaa_nimet_maarat(context, tekija_id, TunnustettuSynti)
        return render(self.request, 'synnit/syntiappi_kuvalla.html', context)
