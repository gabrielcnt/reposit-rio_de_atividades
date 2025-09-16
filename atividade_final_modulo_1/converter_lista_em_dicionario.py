# Criar a lista
# criar a função que irá executar a logica
# colocar um dicionario vazio quer será a conversão da lista
# percorrer os elementos da lista com um looping
# para cada lemento da lista ele irá adicionar ao dicionario como chave o proprio numero
# como valor ele ira adicionar quantas vezes o numero se repete dentro da lista

meu_array = [1, 2, 2, 3, 3, 4, 4, 4, 5, 7, 1]

def converter_lista(lista):
    dicionario = {}
    for n in lista:
        dicionario[n] = lista.count(n)
    return dicionario

print(converter_lista(meu_array))