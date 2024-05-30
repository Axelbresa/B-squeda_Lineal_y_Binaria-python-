def true_false(estado, valor):
    if estado:
        print("El valor si se encuentra en la lista y es:",valor)
    else:
        print("El valor no se encuentra en la lista y era:", valor)


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

busqueda_binaria([1,2,3,4,5,6,7,8,9,10], 10)
busqueda_binaria([1,2,3,4,5,6,7,8,9,10], 11)
