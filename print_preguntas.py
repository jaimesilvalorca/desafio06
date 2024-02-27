import preguntas as p

def print_pregunta(enunciado, alternativas):
    # pregunta = p.pool_preguntas
    print(enunciado[0])
    opciones = ['A', 'B', 'C', 'D']
    for i, alternativa in enumerate(alternativas):
        print(f"{opciones[i]}. {alternativa[0]}")
        
    ###############################################################
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_3']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4