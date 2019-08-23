from .lauriextra import  cap, tarkista_malli 
from django.db import models 

class Syntilaatu(models.Model):
    laatu_nimi = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.laatu_nimi


class Synnintekija(models.Model):
    etunimi = models.CharField(max_length=100)
    sukunimi = models.CharField(max_length=100)

    def __str__(self):
        return cap(self.etunimi)+' '+cap(self.sukunimi)

    def save(self, *args, **kwargs):
#        self.etunimi = cap(self.etunimi)
#        self.sukunimi = cap(self.sukunimi)
        super().save(*args, **kwargs)


#from django.urls import reverse 

class TunnustettuSynti(models.Model):
    tekija = models.ForeignKey(Synnintekija, on_delete=models.CASCADE)
    laatu = models.ForeignKey(Syntilaatu, on_delete=models.CASCADE)
    kpl = models.SmallIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['tekija', 'laatu'], name='kyrsa')
        ]
    
#    def get_absolute_url(self):
#        return reverse('syntiappi_kuvalla')
        
    def save(self, *args, **kwargs):
        self.kpl += tarkista_malli(self.tekija.id, self.laatu, TunnustettuSynti)
        if(self.kpl > 0):
            super().save(*args, **kwargs)

    def __str__(self):
        return str(self.tekija)+' '+str(self.laatu)+', '+str(self.kpl)
