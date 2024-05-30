def true_false(estado, valor):
    if estado:
        print("El valor si se encuentra en la lista y es:",valor)
    else:
        print("El valor no se encuentra en la lista y era:", valor)

def busqueda_secuencial(lista, valor):
    for elemento in lista:
        if elemento == valor:
            true_false(True, valor)
            return
    true_false(False, valor)

busqueda_secuencial([1,2,3,4,5,6,7,8,9,10], 10)
busqueda_secuencial([1,2,3,4,5,6,7,8,9,10], 11)
