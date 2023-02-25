#usamos la funcion def
def x(lista): 
    resultado = []
#   funcion for 
    for n in lista: 
        if n % 5 == 0: 
            resultado.append(n)
    return resultado 
#agregamos la lista 
numeros = [5,150,40,27,89,65,55,80,30]
y = x(numeros)
print(y)