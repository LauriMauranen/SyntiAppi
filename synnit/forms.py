from .models import Synnintekija, Syntilaatu, TunnustettuSynti 
from django.core.cache import cache 
from django.forms import Form, IntegerField, ModelChoiceField, ModelForm  


class SyntiForm(ModelForm):
    class Meta:
        model = TunnustettuSynti
        fields = ['tekija', 'laatu', 'kpl']
        
    def validate_unique(self):
        return True 

