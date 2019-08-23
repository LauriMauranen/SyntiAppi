from .forms import SyntiForm
from .lauriextra import lisaa_nimet_maarat, tee_csv
from .models import Synnintekija, TunnustettuSynti 
from django.shortcuts import render
from django.views.generic.edit import FormView 


class Syntiappi(FormView):
    form_class = SyntiForm 
    template_name = 'synnit/syntiappi_kuvalla.html'
    
    def form_valid(self, form):
        form.save()
        tekija_id = form['tekija'].value()
        context = super().get_context_data()
        context = lisaa_nimet_maarat(context, form, TunnustettuSynti)
        return render(self.request, 'synnit/syntiappi_kuvalla.html', context)


from datetime import datetime
from django.conf import settings
from django.http import FileResponse, HttpResponseRedirect

import os

def lataa_csv(request):
    if(tee_csv(TunnustettuSynti)):
        data = open(os.path.join(settings.MEDIA_ROOT, 'syntitaulukko.csv'), 'r')
        aika = datetime.now().strftime('%d-%m-%Y')
        tiedostonimi = 'syntitaulukko_{}.csv'.format(aika)
        return FileResponse(data, as_attachment=True, filename=tiedostonimi)
    else:
        return HttpResponseRedirect('/')
