from DATABASE import instrument_data
from operations import data_generator


class escala:
    def __init__(self, tom, tipo, s_ou_b):
        self.s_ou_b = s_ou_b
        self.tipo = tipo
        self.tom = tom.upper()

    def graus_e_notas(self):
        # retorna um dicionario contendo todos os graus e notas existentes.
        todos_graus = data_generator.todos_os_graus(self.s_ou_b)
        todas_notas = data_generator.notas_no_tom(self.tom, self.s_ou_b)
        dict = data_generator.dict_grau_nota(todos_graus, todas_notas)
        return dict

    def escala_notas(self):
        escala_graus = data_generator.graus_da_escala(self.tipo, self.s_ou_b)
        graus = self.graus_e_notas()
        escala_em_notas = []
        for grau in escala_graus:
            escala_em_notas.append(graus[grau])
        return escala_em_notas

    def escala_graus(self):
        escala_graus = data_generator.graus_da_escala(self.tipo, self.s_ou_b)
        return escala_graus

    def escala_grau_notas(self):
        dct = {}
        for num, grau in enumerate(self.escala_graus()):
            dct[grau] = self.escala_notas()[num]
        return dct

    def find_possible_chords(self):
        scale_degrees = self.escala_graus()
        acordes = data_generator.acordes()
        usable_chords = []
        for acorde in acordes:
            lst = []
            for degree in acordes[acorde]:
                lst.append(degree)
            s_lst = set(lst)
            s_scl_dgr = set(scale_degrees)
            if s_lst.issubset(s_scl_dgr):
                usable_chords.append(acorde)
        return usable_chords


class guitar_notes:
    def __init__(self, cordas, casas, afinacao):
        self.casas = casas
        self.cordas = cordas
        self.afinacao = afinacao

    def notes_in_strings(self):
        notas_em_0 = instrument_data.notas_afinacao[self.afinacao].upper()
        nts = data_generator.notas_no_tom('e', 's')
        dct_notas_por_corda = {}
        num_nts = len(nts)

        for corda in range(1, self.cordas + 1):
            lst_tuplas = []
            count_note = 0
            nts = data_generator.notas_no_tom(notas_em_0[corda-1], 's')
            for casa in range(self.casas+1):
                if count_note < num_nts-1:
                    lst_tuplas.append((casa, nts[count_note]))
                    count_note += 1
                else:
                    lst_tuplas.append((casa, nts[count_note]))
                    count_note = 0
            dct_notas_por_corda[str(corda)] = lst_tuplas
        return dct_notas_por_corda


def main():
    tom = 'c'
    tipo = 'maior'
    s_ou_b = 's'
    esc = escala(tom, tipo, s_ou_b)

    print(esc.escala_grau_notas())
    print(esc.find_possible_chords())

    instrumento = guitar_notes(6, 12, 'regular')
    notas_cordas = instrumento.notes_in_strings()
    for num, i in enumerate(notas_cordas):
        print(f'Corda {num+1}', instrumento.notes_in_strings()[i])

    # print(notas_cordas)
    nts_cs = []
    for corda in notas_cordas:
        for tupla in notas_cordas[corda]:
            if tom.upper() in tupla:
                nts_cs.append((corda, tupla))

    print(nts_cs)

if __name__ == '__main__':
    main()