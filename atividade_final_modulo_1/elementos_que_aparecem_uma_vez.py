# pegar uma lista com alguns elementos
# criar uma função que receba a lista como parâmetro
# criar uma lista vazia para armazenar os valores unicos
# percorrer a lista e retornar os elementos que aparecem uma vez

array = [1, 2, 2, 1, 3, 3, 4, 5, 5, 6, 6]

def elementos_unicos(lista):
    for n in lista:
        if lista.count(n) == 1:
            return n

print(elementos_unicos(array))
