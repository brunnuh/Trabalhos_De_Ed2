import time
from copy import deepcopy

'''


Introdução:
- Implementar algoritmo de ordenação que receba uma colecão
- A coleção é uma lista de arestas
- Para comparar o peso as arestas entre dois item da coleção basta usar a chave 'weight' (peso)

Exemplos:
- Modo convencional
colecao[i] operador de comparacao colecao[j]
colecao[i] < colecao[j]

- Modo que você vai usar
int(colecao[i]['weight']) operador de comparacao int(colecao[j]['weight'])
int(colecao[i]['weight']) < int(colecao[j]['weight'])

É nescessário converter o valor pra Interger no momento da comparação a fim de evitar erros
'''

# Sua classe algoritmo de ordenação precisar ter um método ordenar
'''class InsertionSort(object):
    def ordenar(self, colecao):
        O método ordenar recebe uma colecão
        realiza ordenacão na colecão
        retorna colecão após ordenação
   
        return colecao'''


class QuickSort(object):
    def ordenar(self, colecao, inicio, tamanho):

        if (inicio < tamanho):
            pos = self.particionar(colecao, inicio, tamanho)
            self.ordenar = (colecao, inicio, pos-1)
            self.ordenar = (colecao, pos + 1, tamanho)
        return colecao

    def particionar(self, colecao, inicio, fim):

        pivoEsq = colecao[inicio]['weight']
        destPivo = inicio
        andarColecao = inicio + 1

        while (andarColecao <= fim):
            if (int(colecao[andarColecao]['weight']) < int(pivoEsq)):
                destPivo += 1
                self.trocar(colecao, destPivo, andarColecao)
            andarColecao += 1
        self.trocar(colecao, inicio, destPivo)
        return destPivo

    def trocar(self, colecao, n, m):
        temp = colecao[n]['weight']
        colecao[n]['weight'] = colecao[m]['weight']
        colecao[m]['weight'] = temp


class MergeSort(object):

    def ordenar(self, colecao, inicio, fim):  # v, p, r
        if (inicio < fim):
            posMeio = (inicio + fim) // 2  # posicao do elemento do meio
            self.ordenar(colecao, inicio, posMeio)  # dividindo a colecao pela esquerda
            self.ordenar(colecao, posMeio + 1, fim)  # dividindo a colecao pela direita
            self.Intercalar(colecao, inicio, posMeio, fim)
        return colecao

    def Intercalar(self, colecao, inicio, Meio, fim):  # v, p, q, r
        colecaoCopia = deepcopy(colecao)
        contEsq = inicio  # contador da colecao esquerda # i
        contDir = Meio + 1  # contador da colecao direita # j
        contCopia = inicio  # contador da copia #k

        while (contCopia <= fim):
            if (contEsq > Meio):
                colecao[contCopia]['weight'] = colecaoCopia[contDir]['weight']
                contDir += 1
            elif (contDir > fim):
                colecao[contCopia]['weight'] = colecaoCopia[contEsq]['weight']
                contEsq += 1
            elif (int(colecaoCopia[contEsq]['weight']) < int(colecaoCopia[contDir]['weight'])):
                colecao[contCopia]['weight'] = colecaoCopia[contEsq]['weight']
                contEsq += 1
            else:
                colecao[contCopia]['weight'] = colecaoCopia[contDir]['weight']
                contDir += 1
            contCopia += 1


class InsertionSort(object):  # complexidade n^2 exponencial
    def ordenar(self, colecao, inicio, fim):
        cont = inicio + 1  # contador principal, comeca pelo 2 item i
        while (cont < fim):
            temp = colecao[cont]['weight']  # variavel com valor atual
            contAnt = cont - 1  # contador sempre atras do contador principal j
            trocou = False
            while (contAnt >= inicio and int(colecao[contAnt]['weight']) > int(
                    temp)):  # troquei o contAnt >= 0 por contAnt >= inicio pra ser usado pelos outros metodos
                colecao[contAnt + 1]['weight'] = colecao[contAnt]['weight']
                trocou = True
                contAnt -= 1
            if (trocou == True):
                colecao[contAnt + 1]['weight'] = temp
            cont += 1
        return colecao


class QuickSortInsertionP(object):

    def ordenar(self, colecao, inicio, tamanho, L):
        if (tamanho == len(colecao) - 1):
            pos = 0
        if (inicio < tamanho):
            if (L != 0):
                pos, L = self.particionar(colecao, inicio, tamanho, L)  # escolher o pivo e trocar
                ordenar = (colecao, inicio, pos - 1)
                ordenar = (colecao, pos + 1, tamanho)
            else:
                InsertionSort(colecao, 0, tamanho)
        return colecao

    def particionar(self, colecao, inicio, fim, L):

        pivoEsq = colecao[inicio]['weight']
        destPivo = inicio
        andarColecao = inicio + 1
        L -= 1
        while (andarColecao < fim):
            if (int(colecao[andarColecao]['weight']) < int(pivoEsq)):
                destPivo += 1
                self.trocar(colecao, destPivo, andarColecao)
            andarColecao += 1
        self.trocar(colecao, inicio, destPivo)
        return destPivo, L

    def trocar(self, colecao, n, m):
        temp = colecao[n]['weight']
        colecao[n]['weight'] = colecao[m]['weight']
        colecao[m]['weight'] = temp


class MergeSortInsertP(object):

    def __init__(self):
        self.posMeio = 0
        self.posposMeio = 0
    def ordenar(self, colecao, inicio, fim, L):  # metodo
        if (inicio < fim):
            if ((fim - inicio) > L): # fim - inicio é o tamanho da colecao atual
                self.posMeio = (inicio + fim) // 2  # posicao do elemento do me
                self.ordenar(colecao, inicio, self.posMeio, L)
                self.ordenar(colecao, self.posMeio + 1, fim, L)
                if(inicio == 0 and fim == len(colecao)-1):
                    InsertionSort.ordenar(self,colecao,inicio,fim)
                    self.posMeio = len(colecao)//2
                elif(inicio == 0 and fim == len(colecao) - 1):
                    return colecao
                else:
                    self.Intercalar(colecao, inicio, self.posMeio, fim)
                    return colecao
            if((fim - inicio) <= L):
                self.posposMeio = self.posMeio
                self.posMeio = (inicio + fim) // 2  # quando ele nao entra no if, ele nao encontra a ultima metada, por isso tem essa
                self.Intercalar(colecao, inicio, self.posMeio, fim)
                self.posMeio = self.posposMeio  # antes de devolver, modificando pra ultima metade
        return colecao


    def Intercalar(self, colecao, inicio, Meio, fim):  # v, p, q, r
        colecaoCopia = deepcopy(colecao)
        contEsq = inicio  # contador da colecao esquerda # i
        contDir = Meio + 1  # contador da colecao direita # j
        contCopia = inicio  # contador da copia #k

        while (contCopia <= fim):
            if (contEsq > Meio):
                colecao[contCopia]['weight'] = colecaoCopia[contDir]['weight']
                contDir += 1
            elif (contDir > fim):
                colecao[contCopia]['weight'] = colecaoCopia[contEsq]['weight']
                contEsq += 1
            elif (int(colecaoCopia[contEsq]['weight']) < int(colecaoCopia[contDir]['weight'])):
                colecao[contCopia]['weight'] = colecaoCopia[contEsq]['weight']
                contEsq += 1
            else:
                colecao[contCopia]['weight'] = colecaoCopia[contDir]['weight']
                contDir += 1
            contCopia += 1
