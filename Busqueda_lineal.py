import time
from True_o_False import true_false

start_time = time.time()

def busqueda_secuencial(lista, valor):
    for elemento in lista:
        if elemento == valor:
            true_false(True, valor)
            return
    true_false(False, valor)

# busqueda_secuencial([1,2,3,4,5,6,7,8,9,10], 10)
# busqueda_secuencial([1,2,3,4,5,6,7,8,9,10], 11)

# end_time = time.time()
# execution_time = end_time - start_time

# print("Tiempo de ejecución: {:.5f} segundos".format(execution_time))
