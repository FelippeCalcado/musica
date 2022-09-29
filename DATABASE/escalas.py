TOM = 2
SEMITOM = 1

ESCALAS_DIATONICAS_S = {
    'maior': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    'menor_natural': ['I', 'II', 'II#', 'IV', 'V', 'V#', 'VI#'],
    'menor_harmonica': ['I', 'II', 'II#', 'IV', 'V', 'V#', 'VII'],
    'menor_melodica': ['I', 'II', 'II#', 'IV', 'V', 'VI', 'VII']
}

INTERVALO_ESCALAS_DIATONICAS = {
    'maior': [0, TOM, TOM, SEMITOM, TOM, TOM, TOM],
    'menor_natural': [0, TOM, SEMITOM, TOM, TOM, SEMITOM, TOM],
    'menor_harmonica': [0, TOM, SEMITOM, TOM, TOM, SEMITOM, TOM+SEMITOM],
    'menor_melodica': [0, TOM, SEMITOM, TOM, TOM, TOM, TOM]
}

ESCALAS_SIMETRICAS_S = {
    'diminuta': ['I', 'II', 'II#', 'IV', 'IV#', 'V#', 'VI', 'VII'],
    'tons_inteiros': ['I', 'II', 'III', 'IV#', 'V#', 'VI#']
}

ESCALAS_PENTATONICAS_S = {
    'pentatonica_maior': ['I', 'II', 'III', 'V', 'VI'],
    'pentatonica_menor': ['I', 'II#', 'IV', 'V', 'VI#'],
}

ESCALAS_BLUES_S = {
    'blues_maior': ['I', 'II', 'II#', 'III', 'V', 'VI'],
    'blues_menor': ['I', 'II#', 'IV', 'IV#', 'V', 'VI#'],
    'info': {'blue_note_maior': 'II#', 'blue_note_menor': 'IV#', }
}

ESCALAS_S = {
           'maior': ESCALAS_DIATONICAS_S['maior'],
           'menor': ESCALAS_DIATONICAS_S['menor_natural'],
           'menor_natural': ESCALAS_DIATONICAS_S['menor_natural'],
           'menor_harmonica': ESCALAS_DIATONICAS_S['menor_harmonica'],
           'menor_melodica': ESCALAS_DIATONICAS_S['menor_melodica'],
           'diminuta': ESCALAS_SIMETRICAS_S['diminuta'],
           'tons_inteiros': ESCALAS_SIMETRICAS_S['tons_inteiros'],
           'pentatonica_maior': ESCALAS_PENTATONICAS_S['pentatonica_maior'],
           'pentatonica_menor': ESCALAS_PENTATONICAS_S['pentatonica_menor'],
           'blues_maior': ESCALAS_BLUES_S['blues_maior'],
           'blues_menor': ESCALAS_BLUES_S['blues_menor']
           }


# BEMOIS
ESCALAS_DIATONICAS_B = {
    'maior': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    'menor_natural': ['I', 'II', 'IIIb', 'IV', 'V', 'VIb', 'VIIb'],
    'menor_harmonica': ['I', 'II', 'IIIb', 'IV', 'V', 'VIb', 'VII'],
    'menor_melodica': ['I', 'II', 'IIIb', 'IV', 'V', 'VI', 'VII']
}

ESCALAS_SIMETRICAS_B = {
    'diminuta': ['I', 'II', 'IIIb', 'IV', 'Vb', 'VIb', 'VI', 'VII'],
    'tons_inteiros': ['I', 'II', 'III', 'Vb', 'VIb', 'VIIb']
}

ESCALAS_PENTATONICAS_B = {
    'pentatonica_maior': ['I', 'II', 'III', 'V', 'VI'],
    'pentatonica_menor': ['I', 'IIIb', 'IV', 'V', 'VIIb'],
}

ESCALAS_BLUES_B = {
    'blues_maior': ['I', 'II', 'IIIb', 'III', 'V', 'VI'],
    'blues_menor': ['I', 'IIIb', 'IV', 'Vb', 'V', 'VIIb'],
    'info': {'blue_note_maior': 'IIIb', 'blue_note_menor': 'Vb', }
}

ESCALAS_B = {
           'maior': ESCALAS_DIATONICAS_B['maior'],
           'menor': ESCALAS_DIATONICAS_B['menor_natural'],
           'menor_natural': ESCALAS_DIATONICAS_B['menor_natural'],
           'menor_harmonica': ESCALAS_DIATONICAS_B['menor_harmonica'],
           'menor_melodica': ESCALAS_DIATONICAS_B['menor_melodica'],
           'diminuta': ESCALAS_SIMETRICAS_B['diminuta'],
           'tons_inteiros': ESCALAS_SIMETRICAS_B['tons_inteiros'],
           'pentatonica_maior': ESCALAS_PENTATONICAS_B['pentatonica_maior'],
           'pentatonica_menor': ESCALAS_PENTATONICAS_B['pentatonica_menor'],
           'blues_maior': ESCALAS_BLUES_B['blues_maior'],
           'blues_menor': ESCALAS_BLUES_B['blues_menor']
           }