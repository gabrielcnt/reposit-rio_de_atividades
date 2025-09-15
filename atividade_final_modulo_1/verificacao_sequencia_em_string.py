letras = 'aaabbbb'

def sequencia_string(string):
    
    letra_b = False
    for l in string:
        if l == 'b':
            letra_b = True
        if l == 'a'and letra_b == True:
            return False
    return True      

print(sequencia_string(letras))