
array = [1, 2, 3, 3, 3, 4, 5]

def frequencia_de_item(lista):
    frequencia = None
    maior_quantidade_repeticoes = 0

    for n in lista:
        if lista.count(n) > maior_quantidade_repeticoes:
            maior_quantidade_repeticoes = lista.count(n)
            frequencia = n

    return frequencia
        

print(frequencia_de_item(array))