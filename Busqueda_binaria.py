import time
from True_o_False import true_false

start_time = time.time()

def busqueda_binaria(lista, valor):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        mitad = (izquierda + derecha) // 2
        
        if lista[mitad] == valor:
            true_false(True, valor)
            return
        elif valor < lista[mitad]:
            derecha = mitad - 1
        else:
            izquierda = mitad + 1

    true_false(False, valor)

# busqueda_binaria([1,2,3,4,5,6,7,8,9,10], 10)
# busqueda_binaria([1,2,3,4,5,6,7,8,9,10], 11)


# end_time = time.time()
# execution_time = end_time - start_time

# print("Tiempo de ejecución: {:.5f} segundos".format(execution_time))