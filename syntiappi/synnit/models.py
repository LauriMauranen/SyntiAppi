from django.db import models

class Syntilaatu(models.Model):
    
    laatu_nimi = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.laatu_nimi

class Synnintekija(models.Model):
    
    etunimi = models.CharField(max_length=100)
    sukunimi = models.CharField(max_length=100)

    def __str__(self):
        return self.etunimi+' '+self.sukunimi

    def save(self, *args, **kwargs):
        self.etunimi = cap(self.etunimi)
        self.sukunimi = cap(self.sukunimi)
        super().save(*args, **kwargs)

class TunnustettuSynti(models.Model):

    tekija = models.ForeignKey(Synnintekija, on_delete=models.CASCADE)
    laatu = models.ForeignKey(Syntilaatu, on_delete=models.CASCADE)
    kpl = models.SmallIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['tekija', 'laatu'], name='kyrsa')
        ]

    def __str__(self):
        return self.tekija.etunimi+' '+self.tekija.sukunimi+', '+self.laatu.laatu_nimi+', '+str(self.kpl)

    def save(self, *args, **kwargs):       
        self.kpl = tarkista_malli(self.tekija.id, 
                                  self.laatu.laatu_nimi, 
                                  self.kpl)

        if(self.kpl > 0):    
            super().save(*args, **kwargs)

def tarkista_malli(tekija_id, laatu_nimi, kpl):
    mahdollinen_tekija = TunnustettuSynti.objects.filter(tekija=tekija_id, 
                                                         laatu=laatu_nimi)
    if  mahdollinen_tekija.exists():
        syyllinen = mahdollinen_tekija.get()            
        kpl += syyllinen.kpl
        syyllinen.delete()

    return kpl

def cap(sana):
    return sana.capitalize()
    

