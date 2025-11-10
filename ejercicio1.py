# AFD que acepta cadenas que contengan "01" y terminen en "0"

adf = {
    'estados': {'a', 'b', 'c', 'd'},
    'alfabeto': {'0', '1'},
    'transiciones': {
        'a': {'0': 'b', '1': 'a'},   # si veo 0 paso a b, si no me quedo
        'b': {'0': 'b', '1': 'c'},   # aquí detecto el 01
        'c': {'0': 'd', '1': 'c'},   # si después de 01 llega 0 paso a d
        'd': {'0': 'd', '1': 'c'}    # si sigo con 0s me quedo, si llega 1 vuelvo
    },
    'estado_inicial': 'a',
    'estados_finales': {'d'}         # solo d es final
}

def evaluacion(adf, palabra):
    estado_actual = adf['estado_inicial']
    for simbolo in palabra:
        # si el símbolo no está en el alfabeto, paro
        if simbolo not in adf['alfabeto']:
            print(f"Alguno de los caracteres {simbolo} no pertenece al alfabeto")
            return False
        # cambio de estado según la transición
        estado_actual = adf['transiciones'][estado_actual][simbolo]
        print(f"{simbolo} > {estado_actual}")  # para ver el recorrido
    # regreso si terminó en un estado válido
    return estado_actual in adf['estados_finales']

# pruebo con una cadena
cadena = "1100110"
print(f"Procesando la cadena {cadena}")
resultado = evaluacion(adf, cadena)
print(f"¿Se aceptó? {resultado}")
