class PesquisaBinaria:

    def pesquisa(self, lista, item):

        baixo = 0
        alto = len(lista) - 1

        while baixo <= alto:
            meio = (baixo + alto) // 2
            chute = lista[meio]

            if chute == item:
                return meio

            if chute > item:
                alto = meio - 1

            else:
                baixo = meio + 1

        return None

if __name__ == "__main__":
    ps = PesquisaBinaria()
    minha_lista = [1, 3, 5, 7, 9]

    print(ps.pesquisa(minha_lista, 3))
    print(ps.pesquisa(minha_lista, -1))
