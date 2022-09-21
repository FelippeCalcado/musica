from operations import generic_functions


def notas_no_tom(tom, b_or_s):
    tom_maiusculo = tom.upper()
    notes = generic_functions.get_data(f'todas_as_notas_{b_or_s}')
    lst = generic_functions.list_reorderer(tom_maiusculo, notes)
    return lst

def graus_da_escala(scale_name):
    return generic_functions.get_data('escala_em_graus')[scale_name]

def dict_grau_nota(graus, escala):
    return generic_functions.dict_creator(graus, escala)