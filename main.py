from ListaLigada import ListaLigada


def teste_adiciona_comeco(name):
    lista_ligada = ListaLigada()

    #lista_ligada.adiciona_comeco('Junior')
    #lista_ligada.adiciona_comeco('Italo')

    lista_ligada.adiciona_fim('Zé')
    lista_ligada.adiciona_fim('Bé')


    print(lista_ligada)

    lista_ligada.adiciona_posicao(2, 'Jú')

    print(lista_ligada)

    print (lista_ligada.contem('Jú'))


    #print(lista_ligada.pegar(1))

    #print(lista_ligada)





if __name__ == '__main__':
    teste_adiciona_comeco('PyCharm')