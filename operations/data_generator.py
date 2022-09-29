from operations import generic_functions


def notas_no_tom(tom, b_or_s):
    tom_maiusculo = tom.upper()
    notes = generic_functions.get_data(f'todas_as_notas_{b_or_s}')
    lst = generic_functions.list_reorderer(tom_maiusculo, notes)
    return lst


def todos_os_graus(b_or_s):
    return generic_functions.get_data(f'todos_os_graus_{b_or_s}')


def graus_da_escala(scale_name, b_or_s):
    return generic_functions.get_data(f'escala_em_graus_{b_or_s}')[scale_name]


def dict_grau_nota(graus, notas):
    return generic_functions.dict_creator(graus, notas)

def acordes():
    return generic_functions.get_data('acordes_em_graus')