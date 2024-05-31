# Importamos la funciona para imprimir si es verdadero o falso
from True_o_False import true_false

# Funcion que le pasamos como parametro una lista de numeros y el valor que queremos buscar
def busqueda_secuencial(lista, valor):
# Recorremos la lista con un for
    for elemento in lista:
# Si el elemento recorrido de la lista es igual a el valor que pasamos como parametros entonces es true
        if elemento == valor:
# Si es true entonces pasamos true y el valor a la otra funcion
            true_false(True, valor)
#Return finaliza la función cuando encontramos el valor
            return
# Si es false entonces pasamos false y el valor a la otra funcion
    true_false(False, valor)

