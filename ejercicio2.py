# AFD que acepta cadenas con número impar de 'b'

adf = {
    'estados': {'1', '2'},
    'alfabeto': {'a', 'b'},
    'transiciones': {
        '1': {'a': '1', 'b': '2'},   # si veo una b paso al estado 2
        '2': {'a': '2', 'b': '1'}    # cada b me cambia de estado
    },
    'estado_inicial': '1',
    'estados_finales': {'2'}          # acepto si termino en 2 (impar de b)
}

def evaluacion(adf, palabra):
    estado_actual = adf['estado_inicial']
    for simbolo in palabra:
        # si hay algo fuera del alfabeto, corto
        if simbolo not in adf['alfabeto']:
            print(f"Alguno de los caracteres {simbolo} no pertenece al alfabeto")
            return False
        # cambio de estado según lo que lea
        estado_actual = adf['transiciones'][estado_actual][simbolo]
        print(f"{simbolo} > {estado_actual}")  # para ver cómo va avanzando
    # veo si acabó en estado final
    return estado_actual in adf['estados_finales']

# probando
cadena = "babb"
print(f"Procesando la cadena {cadena}")
resultado = evaluacion(adf, cadena)
print(f"¿Se aceptó? {resultado}")
