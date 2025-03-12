def ingresar_conjuntos():
    cantidad_conjuntos = int(input("¿Cuántos conjuntos deseas ingresar? "))
    conjuntos = {}
    
    for i in range(cantidad_conjuntos):
        nombre = input(f"Ingrese el nombre del conjunto {i+1}: ")
        conjunto_input = input(f"Ingrese los elementos del conjunto {nombre} (separados por comas): ")
        
        # Validación de los elementos
        conjunto = set(conjunto_input.split(','))
        conjuntos[nombre] = conjunto
    
    return conjuntos


def operar_conjuntos(conjuntos):
    while True:
        print("\nConjuntos disponibles:", ", ".join(conjuntos.keys()))
        print("\nOperaciones disponibles:")
        print("1. Unión")
        print("2. Intersección")
        print("3. Diferencia")
        print("4. Subconjunto")
        print("5. Relación binaria")
        
        operacion = int(input("Elige la operación que deseas realizar (1-5): "))
        nombres_seleccionados = input("Ingresa los nombres de los conjuntos con los que deseas operar (separados por comas): ").split(',')
        nombres_seleccionados = [nombre.strip() for nombre in nombres_seleccionados]
        
        conjuntos_seleccionados = []
        for nombre in nombres_seleccionados:
            if nombre in conjuntos:
                conjuntos_seleccionados.append(conjuntos[nombre])
            else:
                print(f"El conjunto '{nombre}' no es válido.")
        
        if len(conjuntos_seleccionados) < 1:
            print("Debes seleccionar al menos un conjunto para realizar una operación.")
            continue
        
        if operacion == 1:
            resultado = conjuntos_seleccionados[0]
            for c in conjuntos_seleccionados[1:]:
                resultado = resultado.union(c)
            print("Resultado de la unión:", resultado)
        
        elif operacion == 2:
            resultado = conjuntos_seleccionados[0]
            for c in conjuntos_seleccionados[1:]:
                resultado = resultado.intersection(c)
            print("Resultado de la intersección:", resultado)
        
        elif operacion == 3:
            resultado = conjuntos_seleccionados[0]
            for c in conjuntos_seleccionados[1:]:
                resultado = resultado.difference(c)
            print("Resultado de la diferencia:", resultado)
        
        elif operacion == 4:
            if len(conjuntos_seleccionados) != 2:
                print("Se necesita exactamente dos conjuntos para comprobar la relación de subconjunto.")
                continue
            A, C = conjuntos_seleccionados
            if A <= C:
                print(f"{A} es un subconjunto de {C}.")
            else:
                print(f"{A} no es un subconjunto de {C}.")
        
        elif operacion == 5:
            if len(conjuntos_seleccionados) != 2:
                print("Se necesitan exactamente dos conjuntos para comprobar la relación binaria.")
                continue
            A, B = conjuntos_seleccionados
            # Generar todos los pares posibles entre A y B
            r = []
            for z in A:
                for w in B:
                    r.append(f"{z},{w}")
            r_set = set(r)  # Convertir a un conjunto para eliminar duplicados
            print(f"Relación binaria: {r_set}")
        
        else:
            print("Operación no válida.")
            continue
        
        continuar = input("¿Deseas realizar otra operación? (S/N): ").lower()
        if continuar != 'S':
            break


def calculadora_conjuntos():
    while True:
        conjuntos = ingresar_conjuntos()
        operar_conjuntos(conjuntos)
        continuar = input("¿Deseas ingresar más conjuntos? (S/N): ").lower()
        if continuar != 'S':
            break
    print("¡Hasta luego!")


# Iniciar la calculadora
calculadora_conjuntos()
