# Funcion que trae el resultado de una funcion si es verdadero o false y el valor del numero que se estaba buscando
def true_false(estado, valor):
    #Si es verdadero imprime se encuentra en la lista
    if estado:
        print("El valor si se encuentra en la lista y es:",valor)
    #Si es falso imprime no se encuentra en la lista
    else:
        print("El valor no se encuentra en la lista y era:", valor)
