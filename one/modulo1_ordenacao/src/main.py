from grafo import Grafo
from algoritmosDeOrdenacao import *
from utils import *
import timeit
import os




'''
Implemente o algoritmo de ordenação no arquivo algoritmosDeOrdenacao.py
Instruções básicas de como fazer a implementação estão no arquivo algoritmosDeOrdenacao.py
'''


if __name__ == "__main__":

    #algoritmoDeOrdenacao = QuickSort()
    #algoritmoDeOrdenacao = MergeSort()
    #algoritmoDeOrdenacao = InsertionSort()
    #algoritmoDeOrdenacao = MergeSortInsertP()
    #algoritmoDeOrdenacao = MergeSortInsertF()
    #algoritmoDeOrdenacao = HeapSort() # precisa mandar so a colecao e o final - 1

    #arquivoJson = '../grafos/7vertices.json'
    #arquivoDeSaida = '../arvores_geradas/Resultado.txt'
    vertices = ["7", "100", "1000", "10000", "100000"]

    numVert = ''
    while(True):
        numVert = input(str("Quantas Vertices ?(7 - 100000)")).strip()
        if(numVert in vertices):
            break
        else:
            print("Digite uma vertice valida")

    print("=-"*30)
    arquivoJson = '../grafos/'+numVert+'vertices.json'
    arquivoDeSaida = '../arvores_geradas/Resultado.txt'
    grafo = Grafo()

    while(True):
        opcao = input(str("Escolha o tipo de ordenação\n1 - Quick\n2 - Insert\n3 - Merg\n4 - Merg com Insercao parcial\n5 - Merg com Insercao final\n6 - HeapSort\n"+"=-" * 30)).strip()
        if(opcao in "1"):
            algoritmoDeOrdenacao = QuickSort()
            break
        elif(opcao in "2"):
            algoritmoDeOrdenacao = InsertionSort()
            break
        elif(opcao in "3"):
            algoritmoDeOrdenacao = MergeSort()
            break
        elif(opcao in "4"):
            algoritmoDeOrdenacao = MergeSortInsertP()
            break
        elif(opcao in "5"):
            algoritmoDeOrdenacao = MergeSortInsertF()
            break
        elif(opcao in "6"):
            algoritmoDeOrdenacao = HeapSort()
            break
        else:
            print('escolha uma opcao valida')


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

