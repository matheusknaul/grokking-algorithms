
def pesquisa_binaria(lista, item):
    """Função que o livro "Entendo Algoritmos" aborda no
    primeiro capítulo sobre "Pesquisa Binária".
    
    Tem como objetivo, exemplificar o algoritmo de Pesquisa Binária,
    retornando o índice que o "item" ocupa na "lista".

    Args:
        lista (list): lista com números;
        item (int): item a ser checado na lista.

    Returns:
        int(indice): Retorna o indice da conjunto, relativo a posição que item ocupa da lista;
        None: Caso o item não exista na lista.
    """
    baixo = 0
    alto = len(lista) - 1
    
    while baixo <= alto:
    
        meio = (baixo + alto) // 2 #Será arredondado para baixo, caso não for um número par.
        chute = lista[meio]
        
        if chute == item:
            return meio
        
        if chute > item:
            alto = meio - 1
        
        else:
            baixo = meio + 1
            
    return None

minha_lista = [1,3,4,7,9]

print(pesquisa_binaria(minha_lista, -1))