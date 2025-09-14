def modificar_ip(endereco_ip):
    '''
    Modifica um endreço de ip, subistituindo "." por "[.]"

    Parâmetros:
        endereco_ip (str): o ip no formato padrão (ex: "1.1.1.1").

    retorna:
        str: o ip modificado (ex: "1[.]1[.]1[.]1")
    ''' 
    
    endereco_modificado = ''

    for n in endereco_ip:
        if n == '.':
            # A função replace é usada para substituir um elemento por outro
            endereco_modificado += '.'.replace('.', '[.]') 
        else:
            endereco_modificado += n

    return endereco_modificado

print(modificar_ip('1.5.6.1'))