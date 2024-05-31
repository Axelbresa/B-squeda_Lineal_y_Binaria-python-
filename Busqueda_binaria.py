# Importamos la funciona para imprimir si es verdadero o falso
from True_o_False import true_false

# Funcion que le pasamos como parametro una lista de numeros y el valor que queremos buscar
def busqueda_binaria(lista, valor):
#Definimos las variables: 
# Izquierda con el valor minimo de la lista
    izquierda = 0
# Derecha con el valor maximo de la lista
    derecha = len(lista) - 1

# Mientras izquierda sea igual o menor a derecha se seguira ejecutando
    while izquierda <= derecha:
# Sacamos el valor medio de la lista
        mitad = (izquierda + derecha) // 2
# Si valor que traemos como parametro es igual a el valor de lista es true
        if lista[mitad] == valor:
# Si es true entonces pasamos true y el valor a la otra funcion 
            true_false(True, valor)
#Return finaliza la función cuando encontramos el valor
            return
# Si valor es menor al valor de la lista entonces: restara 1 al valor de la lista
        elif valor < lista[mitad]:
            derecha = mitad - 1
# Si valor es mayor al valor de la lista entonces: sumara 1 al valor de la lista
        else:
            izquierda = mitad + 1
# Si es false entonces pasamos false y el valor a la otra funcion 
    true_false(False, valor)

