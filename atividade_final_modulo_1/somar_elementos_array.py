# ter um array com os numeros
# criar a função que receba o array como parametro
# criar a estrutura que conte quantas vezes cada numero aparece
# criar variavel para somar todos os itens unicos
# armazenar em um dicionario o numero como chave e valor a quantidade de vezes que ele aparece
# percorrer o dicionario ou array para verificar quais tem a contagem igual a 1
# fazer a soma dos elementos unicos
# retornar a soma

meu_array = [1, 2, 3, 2, 1, 4, 10]

def somar_elementos_unicos(lista):
    dicionario = {}
    contar_unicos = 0
    for numero in lista:
        dicionario[numero] = lista.count(numero)
        if lista.count(numero) == 1:
            contar_unicos += numero
    
    print(contar_unicos)

somar_elementos_unicos(meu_array)