def lista():
    lista=[]
    n = 0
    while n < 20:
        n1 = int(input('Insira um valor: '))
        lista.append(n1)
        n = n+1
    return lista
def lista_2():
    lista=[]
    n = 0
    while n < 20:
        n1 = int(input('Insira um valor para a segunda lista: '))
        lista.append(n1)
        n = n+1
    return lista

def subtracao(n1,n2):
    n = 0
    lista = []
    while n < 20:
        lista.append(n1[n]-n2[n])
        n = n+1
    return lista
def soma(n1,n2):
    n = 0
    lista = []
    while n < 20:
        lista.append(n1[n]+n2[n])
        n = n+1
    return lista
def multi(n1,n2):
    n = 0
    lista = []
    while n < 20:
        lista.append(n1[n]*n2[n])
        n = n+1
    return lista
l1 = lista()
l2 = lista_2()
l3 = subtracao(l1, l2)
l4 = soma(l1, l2)
l5 = multi(l1, l2)
print(l1,'\n',l2,'\n',l3,'\n',l4,'\n',l5,'\n')