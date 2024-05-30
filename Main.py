from Busqueda_binaria import busqueda_binaria
from Busqueda_lineal import busqueda_secuencial
import time

start_time = time.time()


print("Busqueda binaria")
busqueda_binaria([1,2,3,4,5,6,7,8,9,10], 10)
busqueda_binaria([1,2,3,4,5,6,7,8,9,10], 11)

end_time = time.time()
execution_time = end_time - start_time

print("Tiempo de ejecución: {:.5f} segundos".format(execution_time))

start_time = time.time()

print("Busqueda secuencial")
busqueda_secuencial([1,2,3,4,5,6,7,8,9,10], 10)
busqueda_secuencial([1,2,3,4,5,6,7,8,9,10], 11)

end_time = time.time()
execution_time = end_time - start_time

print("Tiempo de ejecución: {:.5f} segundos".format(execution_time))
