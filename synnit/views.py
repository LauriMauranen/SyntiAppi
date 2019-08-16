from .forms import SyntiForm
from .lauriextra import taulukko_yksi_syntinen
from .models import Synnintekija, TunnustettuSynti  
from django.views.generic.edit import FormView 


class Syntiappi(FormView):
    form_class = SyntiForm
    success_url = 'kuvalla/'
    template_name = 'synnit/syntiappi.html'
    
    def form_valid(self, form):
        form.save()
        tekija_id = form['tekija'].value()
        taulukko_yksi_syntinen(tekija_id, TunnustettuSynti, Synnintekija)
        return super().form_valid(form)


class SyntiappiKuvalla(Syntiappi):
    success_url = '/kuvalla'
    template_name = 'synnit/syntiappi_kuvalla.html'
    





