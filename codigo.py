class Conjunto:
    def __init__(self, elementos):
        self.elementos = set(elementos)

    def union(self, otro):
        return Conjunto(self.elementos.union(otro.elementos))

    def interseccion(self, otro):
        return Conjunto(self.elementos.intersection(otro.elementos))

    def diferencia(self, otro):
        return Conjunto(self.elementos.difference(otro.elementos))

    def complemento(self, universo):
        return Conjunto(universo.elementos.difference(self.elementos))

    def subconjunto(self, otro):
        return self.elementos.issubset(otro.elementos)

    def conjunto_vacio(self):
        return len(self.elementos) == 0

    def relacion_binaria(self, otro):
        # Genera el producto cartesiano A x B
        pares = {(a, b) for a in self.elementos for b in otro.elementos}
        return pares
        impares = {a for a in self.elementos if a % 2 != 0}
        return impares

    def __str__(self):
        return "{" + ", ".join(map(str, self.elementos)) + "}"


def mostrar_menu():
    print("\n------ CALCULADORA DE CONJUNTOS ------")
    print("------ MENÚ DE OPCIONES ------")
    print("1. Unión")
    print("2. Intersección")
    print("3. Diferencia")
    print("4. Complemento")
    print("5. Subconjunto")
    print("6. Verificar conjunto vacío")
    print("7. Relación binaria")
    print("8. Salir")
    print("9. Ingrese nuevos conjuntos")    



def main():
    conjuntos = []
    universo = Conjunto(range(1, 11))  

    # Ingresar hasta 4 conjuntos
    for i in range(4):
        elementos = input(f"Ingrese los elementos del conjunto {i + 1} (separados por comas): ")
        elementos = list(map(int, elementos.split(',')))
        conjuntos.append(Conjunto(elementos))

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción:  ")

        if opcion == '1':
            for i in range(len(conjuntos)):
                for j in range(i + 1, len(conjuntos)):
                    print(f"Unión de Conjunto {i + 1} y Conjunto {j + 1}: {conjuntos[i].union(conjuntos[j])}")

        elif opcion == '2':
            for i in range(len(conjuntos)):
                for j in range(i + 1, len(conjuntos)):
                    print(f"Intersección de Conjunto {i + 1} y Conjunto {j + 1}: {conjuntos[i].interseccion(conjuntos[j])}")

        elif opcion == '3':
            for i in range(len(conjuntos)):
                for j in range(len(conjuntos)):
                    if i != j:
                        print(f"Diferencia de Conjunto {i + 1} - Conjunto {j + 1}: {conjuntos[i].diferencia(conjuntos[j])}")

        elif opcion == '4':
            for i in range(len(conjuntos)):
                print(f"Complemento de Conjunto {i + 1}: {conjuntos[i].complemento(universo)}")

        elif opcion == '5':
            for i in range(len(conjuntos)):
                for j in range(len(conjuntos)):
                    if i != j:
                        comunes = conjuntos[i].elementos.intersection(conjuntos[j].elementos)
                        if comunes:
                            print(f"Elementos comunes entre Conjunto {i + 1} y Conjunto {j + 1}: {comunes}")
                        else:
                            print(f"No hay elementos comunes entre Conjunto {i + 1} y Conjunto {j + 1}: {{}}")

        elif opcion == '6':
            for i in range(len(conjuntos)):
                print(f"¿Conjunto {i + 1} es vacío?: {conjuntos[i].es_vacio()}")

        elif opcion == '7':
            for i in range(len(conjuntos)):
                for j in range(len(conjuntos)):
                    if i != j:
                        pares = conjuntos[i].relacion_binaria(conjuntos[j])
                        print(f"Relación binaria entre Conjunto {i + 1} y Conjunto {j + 1}: {pares}")

        elif opcion == '8':
            print("Saliendo del programa.")
            break

        elif opcion == '9':
            print("Volviendo al inicio")
            break   

        else:
            print("Opción no válida. Intente de nuevo.")
class Conjunto:
    def __init__(self, elementos):
        self.elementos = set(elementos)

    def union(self, otro):
        return Conjunto(self.elementos.union(otro.elementos))

    def interseccion(self, otro):
        return Conjunto(self.elementos.intersection(otro.elementos))

    def diferencia(self, otro):
        return Conjunto(self.elementos.difference(otro.elementos))

    def complemento(self, universo):
        return Conjunto(universo.elementos.difference(self.elementos))

    def es_subconjunto(self, otro):
        return self.elementos.issubset(otro.elementos)

    def es_vacio(self):
        return len(self.elementos) == 0

    def relacion_binaria(self, otro):
        # Generar el producto cartesiano A x B
        pares = {(a, b) for a in self.elementos for b in otro.elementos}
        return pares

    def __str__(self):
        return "{" + ", ".join(map(str, self.elementos)) + "}"


def mostrar_menu():
    print("\n------ CALCULADORA DE CONJUNTOS ------")
    print("------ MENÚ DE OPCIONES ------")
    print("1. Unión")
    print("2. Intersección")
    print("3. Diferencia")
    print("4. Complemento")
    print("5. Subconjunto")
    print("6. Verificar conjunto vacío")
    print("7. Relación binaria")
    print("8. Salir")
    print("9. Ingresar nuevos conjuntos")


def main():
    conjuntos = []
    universo = Conjunto(range(1, 11))  # Universo de 1 a 10

    # Ingresar hasta 4 conjuntos
    for i in range(4):
        elementos = input(f"Ingrese los elementos del conjunto {i + 1} (separados por comas): ")
        elementos = list(map(int, elementos.split(',')))
        conjuntos.append(Conjunto(elementos))

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            for i in range(len(conjuntos)):
                for j in range(i + 1, len(conjuntos)):
                    print(f"Unión de Conjunto {i + 1} y Conjunto {j + 1}: {conjuntos[i].union(conjuntos[j])}")

        elif opcion == '2':
            for i in range(len(conjuntos)):
                for j in range(i + 1, len(conjuntos)):
                    print(f"Intersección de Conjunto {i + 1} y Conjunto {j + 1}: {conjuntos[i].interseccion(conjuntos[j])}")

        elif opcion == '3':
            for i in range(len(conjuntos)):
                for j in range(len(conjuntos)):
                    if i != j:
                        print(f"Diferencia de Conjunto {i + 1} - Conjunto {j + 1}: {conjuntos[i].diferencia(conjuntos[j])}")

        elif opcion == '4':
            for i in range(len(conjuntos)):
                print(f"Complemento de Conjunto {i + 1}: {conjuntos[i].complemento(universo)}")

        elif opcion == '5':
            for i in range(len(conjuntos)):
                for j in range(len(conjuntos)):
                    if i != j:
                        comunes = conjuntos[i].elementos.intersection(conjuntos[j].elementos)
                        if comunes:
                            print(f"Elementos comunes entre Conjunto {i + 1} y Conjunto {j + 1}: {comunes}")
                        else:
                            print(f"No hay elementos comunes entre Conjunto {i + 1} y Conjunto {j + 1}: {{}}")

        elif opcion == '6':
            for i in range(len(conjuntos)):
                print(f"¿Conjunto {i + 1} es vacío?: {conjuntos[i].es_vacio()}")

        elif opcion == '7':
            for i in range(len(conjuntos)):
                for j in range(len(conjuntos)):
                    if i != j:
                        pares = conjuntos[i].relacion_binaria(conjuntos[j])
                        print(f"Relación binaria entre Conjunto {i + 1} y Conjunto {j + 1}: {pares}")

        elif opcion == '8':
            print("Saliendo del programa.")
            break

        elif opcion == '9':
            print("Volviendo al inicio")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
