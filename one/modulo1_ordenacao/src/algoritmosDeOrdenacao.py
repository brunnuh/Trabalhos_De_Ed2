import time
from copy import deepcopy




class QuickSort(object):
    def __init__(self): #montador
        self.NumComp = 0 # numero de comparacoes feitas
        self.NumAtri = 0 # numero de atribuicoes feitas


    def ordenar(self, colecao):
        tamanho = len(colecao) - 1
        self.quick(colecao, 0, tamanho)
        print(f'foram feitas {self.NumComp} comparacoes \nforam feitas {self.NumAtri} atribuicoes')
        return colecao

    def quick(self, colecao, inicio, tamanho):
        if (inicio < tamanho):
            self.NumComp += 1 # se o if for verdadeiro
            pos = self.particionar(colecao, inicio, tamanho)
            self.NumAtri += 1 # atribui o pos
            self.quick(colecao, inicio, (pos-1))# -1
            self.quick(colecao, (pos + 1), tamanho)
        self.NumComp += 1 # se o if for falso
        return colecao

    def particionar(self, colecao, inicio, fim):

        pivoEsq = colecao[inicio]['weight']
        #destPivo = inicio
        i = inicio+1
        f = fim
        self.NumAtri += 3
        while (i <= f):

            if (int(colecao[i]['weight']) <= int(pivoEsq)):
                i += 1
                self.NumAtri += 1
            elif(int(pivoEsq) <= int(colecao[f]['weight'])):
                f -= 1
                self.NumAtri += 1
            else:
                self.trocar(colecao, i, f)
                i += 1
                f -= 1
                self.NumAtri += 2
            self.NumComp += 2
        colecao[inicio]['weight'] = colecao[f]['weight']
        colecao[f]['weight'] = pivoEsq
        self.NumAtri += 2
        #destPivo += 1
        return f

    def trocar(self, colecao, n, m):
        colecao[n]['weight'],colecao[m]['weight'] = colecao[m]['weight'], colecao[n]['weight']
        self.NumAtri += 2



class MergeSort(object):
    def __init__(self):
        self.numAtri = 0
        self.numComp = 0

    def ordenar(self, colecao):
        self.Merg(colecao, 0, len(colecao)-1)
        print(f'foram feitas {self.NumComp} comparacoes \nforam feitas {self.NumAtri} atribuicoes')
        return colecao

    def Merg(self, colecao, inicio, fim):  # v, p, r
        if (inicio < fim):
            self.numComp += 1
            posMeio = (inicio + fim) // 2  # posicao do elemento do meio
            self.numAtri += 1
            self.Merg(colecao, inicio, posMeio)  # dividindo a colecao pela esquerda
            self.Merg(colecao, posMeio + 1, fim)  # dividindo a colecao pela direita
            self.Intercalar(colecao, inicio, posMeio, fim)
        self.numComp += 1
        return colecao

    def Intercalar(self, colecao, inicio, Meio, fim):  # v, p, q, r
        colecaoCopia = deepcopy(colecao)
        contEsq = inicio  # contador da colecao esquerda # i
        contDir = Meio + 1  # contador da colecao direita # j
        contCopia = inicio  # contador da copia #k
        self.numAtri += 4

        while (contCopia <= fim):
            self.numComp += 1
            if (contEsq > Meio):
                colecao[contCopia]['weight'] = colecaoCopia[contDir]['weight']
                contDir += 1
                self.numAtri += 2
            elif (contDir > fim):
                colecao[contCopia]['weight'] = colecaoCopia[contEsq]['weight']
                contEsq += 1
                self.numAtri += 2
            elif (int(colecaoCopia[contEsq]['weight']) < int(colecaoCopia[contDir]['weight'])):
                colecao[contCopia]['weight'] = colecaoCopia[contEsq]['weight']
                contEsq += 1
                self.numAtri += 2
            else:
                colecao[contCopia]['weight'] = colecaoCopia[contDir]['weight']
                contDir += 1
                self.numAtri += 4
            contCopia += 1
            self.numComp += 1
            self.numAtri += 1

class InsertionSort(object):  # complexidade n^2 exponencial
    def __init__(self):
        self.numAtri = 0
        self.numComp = 0

    def ordenar(self, colecao):
        self.Insert(colecao, 0, len(colecao))
        return colecao


    def Insert(self, colecao, inicio, fim):
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



class MergeSortInsertP(object):# ps: testar o tempo novamente
    def __init__(self):
        self.posMeio = 0
        self.posposMeio = 0

    def ordenar(self, colecao):
        L = int(input('Qual o L: '))
        self.Mergp(colecao, 0, len(colecao) - 1, L)
        return colecao


    def Mergp(self, colecao, inicio, fim, L):  # metodo
        if (inicio < fim):
            if ((fim - inicio) > L): # fim - inicio é o tamanho da colecao atual
                self.posMeio = (inicio + fim) // 2  # posicao do elemento do me
                self.Mergp(colecao, inicio, self.posMeio, L)
                self.Mergp(colecao, self.posMeio + 1, fim, L)
                if((inicio == 0 and fim == (len(colecao))-1)or(inicio == 0 and fim == (len(colecao)//2))):# caso estiver com a metade esquerda, made, e se caso ele estiver completo, termine de ordenar
                    InsertionSort.Insert(self,colecao, inicio, fim)
                    self.posMeio = len(colecao)//2
                elif(inicio != 0 or fim != len(colecao)-1):#se o caso acima der falso é pq a colecao esta quebrada
                    return colecao
                else:# se nenhum dos dois acima der verdadeiro, é pq a colecao ja esta ordenada
                    #self.Intercalar(colecao, inicio, self.posMeio, fim)#por preucacao eu dei uma ultima intercalada, mas nao é necessario
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

        while (contCopia < fim):
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

class MergeSortInsertF(object):

    def __init__(self):
        self.posMeio = 0
        self.posposMeio = 0

    def ordenar(self, colecao):
        L = int(input("Tamanho do L:"))
        self.mergF(colecao, 0, len(colecao)-1, L)
        return colecao

    def mergF(self, colecao, inicio, fim, L):  # metodo
        if (inicio < fim):
            if ((fim - inicio) > L): # fim - inicio é o tamanho da colecao atual
                self.posMeio = (inicio + fim) // 2  # meio
                self.mergF(colecao, inicio, self.posMeio, L)
                self.mergF(colecao, self.posMeio + 1, fim, L)
                if(inicio == 0 and fim == len(colecao)-1):#quando a pilha estiver toda desfeita, manda pro insert ordenar
                    InsertionSort.Insert(self,colecao,inicio,fim)
                    self.posMeio = len(colecao)//2
                else:
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


class HeapSort(object):
    def __init__(self):
        self.posMeio = 0
        self.posposMeio = 0

    def ordenar(self, colecao):
        self.Heap(colecao, len(colecao)-1)
        return colecao

    def Heap(self, colecao, n): #heapsort
        self.buildMax(colecao, n)
        for i in range(n, 0, -1):
            colecao[0]['weight'], colecao[i]['weight'] = colecao[i]['weight'], colecao[0]['weight']
            self.maxHeap(colecao,0, i - 1)
        return colecao

    def buildMax(self, colecao, tamanho):
        for i in range(int(tamanho/2), 0, -1):
            self.maxHeap(colecao, i, tamanho)

    def maxHeap(self, colecao, i, tamanho):  # vai deixar o maior no topo
        left = (2*i) + 1
        right = (2*i) + 2
        if((left <= tamanho) and (int(colecao[left]['weight'])  > int(colecao[i]['weight']))):
            max = left
        else:
            max = i

        if((right <= tamanho) and (int(colecao[right]['weight'])  > int(colecao[max]['weight']))):
            max = right

        if(max != i):
            colecao[max]['weight'], colecao[i]['weight'] = colecao[i]['weight'], colecao[max]['weight'] #possivel erro
            self.maxHeap(colecao, max, tamanho)
