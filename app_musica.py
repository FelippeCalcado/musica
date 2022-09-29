from operations import data_generator


def main():
    todos_graus = data_generator.todos_os_graus('s')
    todas_notas = data_generator.notas_no_tom('c', 's')
    dict_grau_notas_tudo = data_generator.dict_grau_nota(todos_graus, todas_notas)
    escala_graus = data_generator.graus_da_escala('menor')
    print(todos_graus)
    print(todas_notas)
    print(dict_grau_notas_tudo)
    print(escala_graus)
    lst = []
    for i in escala_graus:
        lst.append(dict_grau_notas_tudo[i])
    print(lst)


"""
    graus = data_generator.graus_da_escala('maior')
    escala
    data_generator.dict_grau_nota(graus, escala)
"""

if __name__ == '__main__':
    main()