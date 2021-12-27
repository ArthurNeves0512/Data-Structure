#classe e funções utilizadas:
from collections import deque
###### FUNÇÕES E CLASSE#######
class Arvore:
    def __init__(self, dado,) -> None:
        self.dado = dado
        self.dir = None
        self.esq = None

def prioridade(objeto):
    return len(objeto[1])

def codificar(letra, dicionario):
    if letra in dicionario:
        return dicionario[letra]

def decodificar(arvore, lista):
    if len(lista)>1:   
        if lista[0]=='.':
            if arvore.esq:
                return decodificar(arvore.esq, lista[1:])
        else:
            if arvore.dir:
                return decodificar(arvore.dir, lista[1:])
    else:
        if lista =='.':
            if arvore.esq:
                return arvore.esq.dado
        else:
            if arvore.dir:
                return arvore.dir.dado

def mostra(root):
    fila = deque()
    fila.append(root)
    while fila:
        n = fila.popleft()
        print(n.dado ,end=' ')
        if n.esq:
            fila.append(n.esq)
        if n.dir:
            fila.append(n.dir)

def adicionar(root,no, l):
    if no[0] == '.' and  not root.esq :
        if len(no)>1:
            root.esq =Arvore('*')
            adicionar(root.esq, no[1:], l)
        else:    
            root.esq = l
    elif no[0] == '-' and not root.dir:
        if len(no)>1:
            root.dir = Arvore('*')
            adicionar(root.dir, no[1:], l)
        else:
            root.dir = l
    elif no[0] == '.' and root.esq:
        adicionar(root.esq, no[1:], l)
    elif no[0] == '-' and root.dir:
        adicionar(root.dir, no[1:], l)

##############################

dic = {}
letras = []
tamanho = int(input())
flag = True
strin = ''
possivel = True
for l in range(tamanho):
    letras.append(input().split())

letras = sorted(letras, key = prioridade)
raiz = Arvore('*')

for letra in letras :
    m = Arvore(letra[0])
    adicionar(raiz,letra[1], m)
    dic[letra[0]] = letra[1]
caso =int(input())
teste = input().split()

if caso:
    i = 0
    while i< len(teste):
        for letra in teste[i]:
            codificado = codificar(letra, dic)
            if codificado is not None:
                strin += codificado + ' '
            else:
                possivel= False
                strin = 'Impossível codificar a mensagem!'
                flag = False
                break
        if flag and i< len(teste)-1:
            strin +='/'
        elif not flag:
            break
        i += 1
    print(strin)
else:
    for k in teste:
        if k[0] == '/':
            strin += ' '
            m = decodificar(raiz, k[1:])
            if '*' == m or m is None:
                possivel= False
                strin = 'Impossível decodificar a mensagem!'
                break
            strin += m
        else:
            m = decodificar(raiz, k)
            if '*' == m or m is None:
                possivel= False
                strin = 'Impossível decodificar a mensagem!'
                break
            strin += m
    print(strin)

if possivel:
    mostra(raiz)




