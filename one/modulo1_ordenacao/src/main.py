from grafo import Grafo
from algoritmosDeOrdenacao import *
from utils import *
import timeit



'''
Implemente o algoritmo de ordenação no arquivo algoritmosDeOrdenacao.py
Instruções básicas de como fazer a implementação estão no arquivo algoritmosDeOrdenacao.py
'''


if __name__ == "__main__":

    #algoritmoDeOrdenacao = QuickSort()

    #algoritmoDeOrdenacao = MergeSort()
    #algoritmoDeOrdenacao = InsertionSort()
    #algoritmoDeOrdenacao = QuickSortInsertionP() 0.004
    algoritmoDeOrdenacao = MergeSortInsertP()
    #algoritmoDeOrdenacao = HeapSort()

    arquivoJson = '../grafos/1000vertices.json'
    arquivoDeSaida = '../arvores_geradas/Resultado.txt'

    grafo = Grafo()


    grafo.estabelecerAlgoritmoDeOrdencao(algoritmoDeOrdenacao)
    grafo.carregarGrafo(arquivoJson)

    antes = timeit.default_timer()
    arvoreGeradoraMinima = grafo.executarKruskal()
    depois = timeit.default_timer()
    tempo = (depois-antes)

    SalvarArvoreGeradoraMinimaEmArquivo(arquivoDeSaida, arvoreGeradoraMinima)



    if('QuickSort' in str(algoritmoDeOrdenacao)[23:36]):
        print('O tempo de execucao do algoritmo QuickSort', end=' ')
    elif('MergeSort' in str(algoritmoDeOrdenacao)[23:36]):
        print('O tempo de execucao do algoritmo MergeSort', end=' ')
    else:
        print('O tempo de execucao do algoritmo InsertSort ', end=' ')

    print(f'foi de {tempo:.4f} SEGUNDOS do algoritmo ')

