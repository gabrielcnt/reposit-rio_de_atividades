lista = [1, 3, 4, 5, 6] # lista com valores
dicionario = {} # dicionario vazio para conversão

for num in lista: # looping que percorre cada elemento da lista
    # adiciona o elemento da lista como chave e o elemento da lista multiplicado por 2 como valor
    dicionario[num] = num * 2 

print(dicionario)