from operations import generic_functions


def notas_no_tom(tom, todas_as_notas):
    tom_maiusculo = tom.upper()
    sequencia = generic_functions.reordered_list(tom_maiusculo, todas_as_notas)
    return sequencia


def grau_nota(graus, notas):
    dic_grau_nota = {}
    for num, grau in enumerate(graus):
        dic_grau_nota[grau] = notas[num]
    return dic_grau_nota
