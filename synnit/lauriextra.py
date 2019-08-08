import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

from django.conf import settings
from synnit.models import TunnustettuSynti

def length(x):
    if(np.isscalar(x)):
        pituus = 1
    else:
        pituus = len(x)
    return pituus

def tee_csv(tunnustettu_synti_lista):
    
    rivit = []
    sarakkeet = []
    
    for synti in tunnustettu_synti_lista:
        
        t_nimi = synti.tekija.etunimi+' '+synti.tekija.sukunimi
        l_nimi = synti.laatu.laatu_nimi

        if t_nimi not in rivit:
            rivit.append(t_nimi)
        
        if l_nimi not in sarakkeet:
            sarakkeet.append(l_nimi)
        
        if(len(rivit) == 1 and len(sarakkeet) == 1):
            data = np.reshape(synti.kpl, newshape=(1,1))

        if (len(data) < len(rivit)):
            uusi_rivi = np.zeros(shape=(1,length(data[0])))
            data = np.append(data, uusi_rivi, axis=0)

        if(length(data[0]) < len(sarakkeet)):
            uusi_sarake = np.zeros(shape=(len(data),1))
            data = np.append(data, uusi_sarake, axis=1)
        
        r_ind = rivit.index(t_nimi)
        s_ind = sarakkeet.index(l_nimi)
        data[r_ind,s_ind] = synti.kpl

    df = pd.DataFrame(data, index=rivit, columns=sarakkeet)
    df.sort_index(axis=0, inplace=True)
    df.sort_index(axis=1, inplace=True)
    df.to_csv(path_or_buf='data/testi.csv')

def taulukko_yksi_syntinen(synnintekija):
    
    syntilista = TunnustettuSynti.objects.filter(tekija=synnintekija)
    
    path = settings.MEDIA_ROOT
    filename = 'taulukko_syntinen.png'

    if not syntilista.exists():
        return False

    synnit_nimi = []
    synnit_maara = []
    
    for synti in syntilista.all():
        synnit_nimi.append(synti.laatu.laatu_nimi)
        synnit_maara.append(synti.kpl)

    synnit_nimi = [sana.lower() for sana in synnit_nimi]
    
    fig, ax = plt.subplots()
    
    plöö = np.arange(len(synnit_maara))

    ax.barh(plöö, synnit_maara)
    ax.set_yticks(plöö)
    ax.set_yticklabels(synnit_nimi)
    ax.invert_yaxis()
    ax.set_xlabel("kpl")
    ax.set_title("{} {} tehnyt syntiä".format(synnintekija.etunimi, synnintekija.sukunimi))
    
    fig.savefig(os.path.join(path, filename))
    return True

from django.core.cache import cache
from numpy.random import randint

def aseta_cache_tarkistus(palauta=False):
    luku = randint(2, 1000)
    cache.set('tarkistusluku_cache', luku)
    if(palauta):
        return luku









