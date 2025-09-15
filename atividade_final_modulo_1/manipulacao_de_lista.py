'''
◦ k) Explique o funcionamento do método sum() em uma lista de
inteiros.
'''

lista = []

lista.append(10)
lista.append(20)
lista.append(30)

lista.pop(1)
lista.pop(0)
print(lista)

'''
- O método append() é usado para inserir itens em uma lista
- O método pop() é usado para remover um item da lista (por padrão ele apaga o ultimo item caso não passe um indice como parâmetro)
- O método insert() é usado para adicionar um item em determinada posição na lista informando como parâmetro a posição e o valor
- O método sort() é usado para ordenar uma lista em ordem crescente ou decrescente
- O método count() é usado para contar quantas vezes um determinado item aparece na lista
- O uma função sum() soma todos os itens existentes dentro de uma lista
'''