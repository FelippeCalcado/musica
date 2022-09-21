from operations import data_generator
from DATABASE import notas, escalas, acordes

dict_data = {
    'todas_as_notas_b': notas.NOTAS_B,
    'todas_as_notas_s': notas.NOTAS_S,
    'todos_os_graus': notas.GRAUS,
    'escala_em_graus': escalas.ESCALAS,
    'acordes_em_graus': acordes.TIPOS_DE_ACORDE_DICT,
    'notas_no_tom': data_generator.notas_no_tom,
}


"""
dict_data = {
    'todas_as_notas_b': notas.NOTAS_B,
    'todas_as_notas_s': notas.NOTAS_S,
    'todos_os_graus': notas.GRAUS,
    'escala_em_graus': escalas.ESCALAS,
    'acordes_em_graus': acordes.TIPOS_DE_ACORDE_DICT,
    'notas_no_tom': data_generator.notas_no_tom,
    'graus_notas': data_generator.grau_nota
}"""
# TESTES

def print_data(data):
    print(data)

if __name__ == '__main__':
    tone = 'c'
    notas_em_bemol = data['todas_as_notas_b']
    notas_em_sustenidos = data['todas_as_notas_s']
    todos_os_graus = data['todos_os_graus']
    escala_maior = data['escala_em_graus']['menor']
    acorde = data['acordes_em_graus']
    sequencia_notas_no_tom = data['notas_no_tom'](tone, notas_em_bemol)
    graus_e_notas = data['graus_notas'](todos_os_graus, sequencia_notas_no_tom)

    for acrd in acordes.TIPOS_DE_ACORDE:
        str1 = acrd.ljust(15, ' ')
        str2 = acorde[acrd]
        print_data(f'{tone}{str1}{str2}')
    print(escala_maior)
    print(graus_e_notas)
    for i in escala_maior:
        print(i, graus_e_notas[i])