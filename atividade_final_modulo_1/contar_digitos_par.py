
# criar uma lista com uma quantidade de itens
# criar a função onde q recebera essa lista como parâmetro
# criar um contador para armazenar a quantidade de numeros com digitos pares
# criar um for para percorrer a lista
# criar uma condição para q se a quantidade de digitos for par, será iterado com a variavel
# na condicional o item será convertido para string e retornara o tamanho do item

# a função len() é usada contar a quantidade de itens de uma lista ou string

numeros = [12, 342, 345, 2, 8, 7896, 1976]

def contar_pares(lista):

    contador = 0
    for item in lista:
        if len(str(item)) % 2 == 0:
            contador +=1
    return contador

print(contar_pares(numeros))