from grafo import Grafo
from algoritmosDeOrdenacao import *
from utils import *
import time



'''
Implemente o algoritmo de ordenação no arquivo algoritmosDeOrdenacao.py
Instruções básicas de como fazer a implementação estão no arquivo algoritmosDeOrdenacao.py
'''


if __name__ == "__main__":

    algoritimoDeOrdenacao = QuickSort()
    #algoritimoDeOrdenacao = MergeSort()
    #algoritimoDeOrdenacao = InsertionSort()
    #algoritimoDeOrdenacao = QuickSortInsertionP()

    arquivoJson = '../grafos/100vertices.json'
    arquivoDeSaida = '../arvores_geradas/Resultado.txt'

    grafo = Grafo()
    antes = time.time()

    grafo.estabelecerAlgoritmoDeOrdencao(algoritimoDeOrdenacao)
    grafo.carregarGrafo(arquivoJson)
    arvoreGeradoraMinima = grafo.executarKruskal()

    depois = time.time()
    tempo = (depois - antes)
    SalvarArvoreGeradoraMinimaEmArquivo(arquivoDeSaida, arvoreGeradoraMinima)



    if('QuickSort' in str(algoritimoDeOrdenacao)[23:36]):
        print('O tempo de execucao do algoritmo QuickSort', end=' ')
    elif('MergeSort' in str(algoritimoDeOrdenacao)[23:36]):
        print('O tempo de execucao do algoritmo MergeSort', end=' ')
    else:
        print('O tempo de execucao do algoritmo InsertSort ', end=' ')

    print(f'foi de {tempo:.3f} Segundos.ms do algoritmo ')

