# AFD que acepta cadenas sin la subcadena "11"

adf = {
    'estados': {'a', 'b', 'c'},
    'alfabeto': {'0', '1'},
    'transiciones': {
        'a': {'0': 'a', '1': 'b'},   # si veo un 1 paso a b
        'b': {'0': 'a', '1': 'c'},   # si veo otro 1 seguido voy a c (ya no se acepta)
        'c': {'0': 'c', '1': 'c'}    # c es trampa, ya cayó en "11"
    },
    'estado_inicial': 'a',
    'estados_finales': {'a', 'b'}    # acepto si no llego a c
}

def evaluacion(adf, palabra):
    estado_actual = adf['estado_inicial']
    for simbolo in palabra:
        # si hay algo fuera del alfabeto, paro
        if simbolo not in adf['alfabeto']:
            print(f"Alguno de los caracteres {simbolo} no pertenece al alfabeto")
            return False
        # cambio de estado según el símbolo
        estado_actual = adf['transiciones'][estado_actual][simbolo]
        print(f"{simbolo} > {estado_actual}")  # para ver el recorrido
    # regreso True si termino en un estado válido
    return estado_actual in adf['estados_finales']

# probando
cadena = "110010"
print(f"Procesando la cadena {cadena}")
resultado = evaluacion(adf, cadena)
print(f"¿Se aceptó? {resultado}")
