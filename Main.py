# Importamos las funciones de búsqueda binaria y secuencial
from Busqueda_binaria import busqueda_binaria
from Busqueda_lineal import busqueda_secuencial

# Importamos el paquete time para medir el tiempo de ejecución
import time

# Registramos el tiempo inicial antes de la búsqueda binaria
start_time = time.time()

# Imprimimos el mensaje indicando que empieza la búsqueda binaria
print("Busqueda binaria")

# Realizamos la búsqueda binaria para encontrar el número 10 y 11 en la lista
busqueda_binaria([1,2,3,4,5,6,7,8,9,10], 10)
busqueda_binaria([1,2,3,4,5,6,7,8,9,10], 11)

# Registramos el tiempo final después de las búsquedas binarias
end_time = time.time()

# Calculamos el tiempo de ejecución para las búsquedas binarias
execution_time = end_time - start_time

# Imprimimos el tiempo de ejecución de las búsquedas binaria

print("Tiempo de ejecución: {:.5f} segundos".format(execution_time))

# Realizamos el mismo procedimiento que hicimos en busqueda secuencial
start_time = time.time()

print("Busqueda secuencial")

busqueda_secuencial([1,2,3,4,5,6,7,8,9,10], 10)

busqueda_secuencial([1,2,3,4,5,6,7,8,9,10], 11)

end_time = time.time()

execution_time = end_time - start_time

print("Tiempo de ejecución: {:.5f} segundos".format(execution_time))
