
dicionario = {}

dicionario['a'] = 410
dicionario['b'] = 3
dicionario['b'] = 4
dicionario['c'] = 56
dicionario.pop('b', 3)
dicionario.pop('b', 4)
print(dicionario)

'''
- O update() é usado para atualizar ou adicionar itens em um dicionario
- O pop(chave) remove e retorna o valor de uma chave expecifica
- O get(chave, valor_padrao=None) é usado para pegar o valor de uma chave, caso a chave não exista
ele retorna None
- O keys() retorna somente as chaves de um dicionario
- O values() retorna somente os valores das chaves de um dicionario
- O items() retorna a chave e os valores de suas respectivas chaves
'''