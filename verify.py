import preguntas as p


def verificar(alternativas, eleccion):
    # Devuelve el índice de elección dada
    eleccion = ['a', 'b', 'c', 'd'].index(eleccion)

    # Generar lógica para determinar respuestas correctas
    for indice, opcion in enumerate(alternativas):
        if opcion[1] == 1:
            correcto = indice  # devuelve la posicion con la anternativa correcta

    # Compara la elección del usuario con la alternativa correcta
    if eleccion == correcto:
        print("Respuesta Correcta")
        return True
    else:
        print("Respuesta Incorrecta")
        return False
    
if __name__ == '_main_':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)