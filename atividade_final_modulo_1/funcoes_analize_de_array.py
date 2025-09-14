
lista = [1, 5, 33, 8, 77, 43, 124, 6, 8, 99]

def menor_valor(lista):
    return min(lista)

def maior_valor(lista):
    return max(lista)

def soma_menor_com_maior_valor(lista):
    lista.sort()
    soma = lista[0] + lista[-1]
    return soma

def somar_todos_valores(lista):
    return sum(lista)

def media_dos_valores(lista):
    return sum(lista) / len(lista)

print(menor_valor(lista))
print(maior_valor(lista))
print(soma_menor_com_maior_valor(lista))
print(somar_todos_valores(lista))
print(media_dos_valores(lista))
