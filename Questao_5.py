def inverter_string(s):
    lista_caracteres = list(s)
    
    inicio = 0
    fim = len(lista_caracteres) - 1
    
    while inicio < fim:
        lista_caracteres[inicio], lista_caracteres[fim] = lista_caracteres[fim], lista_caracteres[inicio]
        inicio += 1
        fim -= 1
    
    return ''.join(lista_caracteres)

entrada = input("Digite a string para inverter: ")

resultado = inverter_string(entrada)
print(f"String invertida: {resultado}")
