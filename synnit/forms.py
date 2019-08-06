from django import forms
from django.forms import ModelForm

from synnit.models import Syntilaatu, Synnintekija, TunnustettuSynti

class SyntiForm(ModelForm):
    class Meta:
        model = TunnustettuSynti
        fields = ['tekija', 'laatu', 'kpl']

    def validate_unique(self):
        return
