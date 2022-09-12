TOM = 2
SEMITOM = 1

ESCALAS_DIATONICAS = {
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

ESCALAS_SIMETRICAS = {
    'diminuta': ['I', 'II', 'II#', 'IV', 'IV#', 'V#', 'VI', 'VII'],
    'tons_inteiros': ['I', 'II', 'III', 'IV#', 'V#', 'VI#']
}

ESCALAS_PENTATONICAS = {
    'pentatonica_maior': ['I', 'II', 'III', 'V', 'VI'],
    'pentatonica_menor': ['I', 'II#', 'IV', 'V', 'VI#'],
}

ESCALAS_BLUES = {
    'blues_maior': ['I', 'II', 'II#', 'III', 'V', 'VI'],
    'blues_menor': ['I', 'II#', 'IV', 'IV#', 'V', 'VI#'],
    'info': {'blue_note_maior': 'II#', 'blue_note_menor': 'IV#', }
}

ESCALAS = {
           'maior': ESCALAS_DIATONICAS['maior'],
           'menor': ESCALAS_DIATONICAS['menor_natural'],
           'menor_natural': ESCALAS_DIATONICAS['menor_natural'],
           'menor_harmonica': ESCALAS_DIATONICAS['menor_harmonica'],
           'menor_melodica': ESCALAS_DIATONICAS['menor_melodica'],
           'diminuta': ESCALAS_SIMETRICAS['diminuta'],
           'tons_inteiros': ESCALAS_SIMETRICAS['tons_inteiros'],
           'pentatonica_maior': ESCALAS_PENTATONICAS['pentatonica_maior'],
           'pentatonica_menor': ESCALAS_PENTATONICAS['pentatonica_menor'],
           'blues_maior': ESCALAS_BLUES['blues_maior'],
           'blues_menor': ESCALAS_BLUES['blues_menor']
           }
