def cap(sana):
    return sana.capitalize()


def lisaa_nimet_maarat(context, form, tunnustettusynti_malli):

    tekija_id = form['tekija'].value()
    syntilista = tunnustettusynti_malli.objects.filter(tekija=tekija_id)

    if syntilista.exists():
        
        synnit_nimi = []
        synnit_maara = []
        
        for synti in syntilista.all():
            synnit_nimi.append(synti.laatu.laatu_nimi)
            synnit_maara.append(synti.kpl)
        
        context['synnit_nimi'] = synnit_nimi
        context['synnit_maara'] = synnit_maara
        context['synnintekija'] = syntilista.first().tekija
        context['laatu'] = form['laatu'].value()
        context['kpl'] = form['kpl'].value()

    return context 


import numpy as np 

def length(x):
    if(np.isscalar(x)):
        pituus = 1
    else:
        pituus = len(x)
    return pituus


def tarkista_malli(tekija_id, laatu, malli):

    vastaus = 0

    mahdollinen_tekija = malli.objects.filter(tekija=tekija_id, laatu=laatu)

    if  mahdollinen_tekija.exists():
        syyllinen = mahdollinen_tekija.get()
        vastaus = syyllinen.kpl
        syyllinen.delete()

    return vastaus 


import pandas as pd

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
