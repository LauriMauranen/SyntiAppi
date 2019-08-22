from .models import TunnustettuSynti 
from django.forms import ModelForm  


class SyntiForm(ModelForm):
    class Meta:
        model = TunnustettuSynti
        fields = ['tekija', 'laatu', 'kpl']
        
    def validate_unique(self):
        return True 

