from DATABASE import notas, escalas, acordes

data = {
    'notas_b': notas.NOTAS_B,
    'notas_s': notas.NOTAS_S,
    'graus': notas.GRAUS,
    'escalas': escalas.ESCALAS,
    'acordes': acordes.TIPOS_DE_ACORDE_DICT
}



# TESTES

def print_data(data):
    print(data)

if __name__ == '__main__':
    notas_em_sustenidos = data['notas_s']
    notas_em_bemol = data['notas_b']
    todos_os_graus = data['graus']
    escala_maior = data['escalas']['maior']
    acorde = data['acordes']

    print_data(notas_em_sustenidos)
    tone = 'D'
    for acrd in acordes.TIPOS_DE_ACORDE:
        str1 = acrd.ljust(15, ' ')
        str2 = acorde[acrd]
        print_data(f'{tone}{str1}{str2}')