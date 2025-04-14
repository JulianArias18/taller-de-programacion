#ejercicio 1#
def maximo_de_tres(a, b, c):
    return max(a, b, c)

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

print("El valor máximo es:", maximo_de_tres(a, b, c))

#ejercicio 2#
def maximo_de_tres(a, b, c):
    return max(a, b, c)
numeros = []
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)
maximo_total = numeros[0]
for i in range(1, len(numeros), 2):
    if i+1 < len(numeros):
        maximo_total = maximo_de_tres(maximo_total, numeros[i], numeros[i+1])
    else:
        maximo_total = max(maximo_total, numeros[i])

print("El valor máximo entre los 10 números es:", maximo_total)

#ejercicio 3#
def cargar_vector(nombre):
    n = int(input(f"Ingrese la cantidad de elementos del vector {nombre}: "))
    vector = []
    for i in range(n):
        valor = int(input(f"{nombre}[{i}]: "))
        vector.append(valor)
    return vector

def suma_vector(v):
    return sum(v)

def suma_vectores(a, b):
    return [a[i] + b[i] for i in range(len(a))]

A = cargar_vector("A")
B = cargar_vector("B")

print("Suma de elementos de A:", suma_vector(A))
print("Suma de elementos de B:", suma_vector(B))

if len(A) == len(B):
    C = suma_vectores(A, B)
    print("Vector resultante de la suma A + B:", C)
else:
    print("No se pueden sumar los vectores porque tienen distinta longitud.")

#ejercicio 4#
def potencia(x, k):
    return x ** k

def cantidad_digitos(x):
    return len(str(abs(x)))

def es_capicua(x):
    return str(x) == str(x)[::-1]

def menu_operaciones():
    while True:
        print("\n--- MENÚ DE OPERACIONES NUMÉRICAS ---")
        print("a) Calcular potencia (x^k)")
        print("b) Calcular cantidad de dígitos")
        print("c) Verificar si es capicúa")
        print("x) Salir")

        opcion = input("Elija una opción: ").lower()

        if opcion == "a":
            x = int(input("Ingrese base x: "))
            k = int(input("Ingrese exponente k: "))
            print(f"{x}^{k} = {potencia(x, k)}")

        elif opcion == "b":
            x = int(input("Ingrese un número: "))
            print(f"Cantidad de dígitos: {cantidad_digitos(x)}")

        elif opcion == "c":
            x = int(input("Ingrese un número: "))
            if es_capicua(x):
                print("Es capicúa.")
            else:
                print("No es capicúa.")

        elif opcion == "x":
            print("Fin del programa.")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

menu_operaciones()
 #ejercicio 5#
 def calcular_potencia(x, k):
    return x ** k

def cantidad_digitos(x):
    return len(str(abs(x)))

def es_capicua(x):
    return str(x) == str(x)[::-1]

def menu_operaciones():
    while True:
        print("\n--- MENÚ DE OPERACIONES NUMÉRICAS ---")
        print("a) Calcular potencia (x^k)")
        print("b) Calcular cantidad de dígitos")
        print("c) Verificar si es capicúa")
        print("x) Salir")

        opcion = input("Elija una opción: ").lower()

        if opcion == "a":
            x = int(input("Ingrese base x: "))
            k = int(input("Ingrese exponente k: "))
            print(f"{x}^{k} = {calcular_potencia(x, k)}")

        elif opcion == "b":
            x = int(input("Ingrese un número: "))
            print(f"Cantidad de dígitos: {cantidad_digitos(x)}")

        elif opcion == "c":
            x = int(input("Ingrese un número: "))
            if es_capicua(x):
                print("Es capicúa.")
            else:
                print("No es capicúa.")

        elif opcion == "x":
            print("Fin del programa.")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

menu_operaciones()

#ejercicio 6#
def cargar_matriz(m, n):
    return [[int(input(f"A[{i}][{j}]: ")) for j in range(n)] for i in range(m)]

def sumar_matrices(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def producto_matrices(a, b):
    return [[a[i][j] * b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

def menu_matrices():
    m = int(input("Filas: "))
    n = int(input("Columnas: "))
    print("Cargar matriz A:")
    a = cargar_matriz(m, n)
    print("Cargar matriz B:")
    b = cargar_matriz(m, n)

    opcion = input("¿Sumar (s) o multiplicar (m)?: ").lower()
    if opcion == "s":
        c = sumar_matrices(a, b)
    else:
        c = producto_matrices(a, b)

    print("Resultado (matriz C):")
    mostrar_matriz(c)

menu_matrices()

#ejercicio 7#
import math

def cargar_matriz_cuadrada(n):
    return [[int(input(f"[{i}][{j}]: ")) for j in range(n)] for i in range(n)]

def suma_diagonal(matriz):
    return sum(matriz[i][i] for i in range(len(matriz)))

def filtrar_factoriales(matriz, suma_diag):
    elementos = [matriz[i][j] for i in range(len(matriz)) for j in range(len(matriz))]
    return [x for x in elementos if math.factorial(x) >= suma_diag]

def eliminar_repetidos(vector):
    return list(set(vector))

def ordenar_vector(vector):
    return sorted(vector)

def procesar_matriz():
    n = int(input("Tamaño de la matriz (n x n): "))
    matriz = cargar_matriz_cuadrada(n)
    suma_diag = suma_diagonal(matriz)
    print(f"Suma diagonal principal = {suma_diag}")
    vector = filtrar_factoriales(matriz, suma_diag)
    print("Vector con factoriales filtrados:", vector)
    vector = eliminar_repetidos(vector)
    print("Sin repetidos:", vector)
    vector = ordenar_vector(vector)
    print("Ordenado:", vector)

procesar_matriz()

 #ejercicio 8#
def cargar_electrodomesticos():
    matriz = []
    while True:
        nombre = input("Nombre: ")
        proveedor = input("Proveedor: ")
        while True:
            try:
                precio = int(input("Precio: "))
                stock = int(input("Stock: "))
                break
            except:
                print("Ingrese valores numéricos.")
        matriz.append([nombre, proveedor, str(precio), str(stock)])
        if input("¿Agregar otro? (s/n): ").lower() != "s":
            break
    return matriz

def mostrar_proveedor(matriz, proveedor):
    for fila in matriz:
        if fila[1].lower() == proveedor.lower():
            print(fila[0])

def mostrar_menor_precio(matriz):
    menor = min(matriz, key=lambda x: int(x[2]))
    print("Menor precio:", menor)

def mostrar_stock_positivo(matriz):
    for fila in matriz:
        if int(fila[3]) > 0:
            print(fila)

def menu_electrodomesticos():
    matriz = cargar_electrodomesticos()
    while True:
        print("\n--- MENÚ ELECTRODOMÉSTICOS ---")
        print("a) Mostrar por proveedor")
        print("b) Mostrar menor precio")
        print("c) Mostrar con stock positivo")
        print("x) Salir")
        op = input("Opción: ").lower()
        if op == "a":
            proveedor = input("Proveedor: ")
            mostrar_proveedor(matriz, proveedor)
        elif op == "b":
            mostrar_menor_precio(matriz)
        elif op == "c":
            mostrar_stock_positivo(matriz)
        elif op == "x":
            break

menu_electrodomesticos()
 
#ejercicio 9#
def menu_pacientes():
    lista = []
    while True:
        print("\n--- MENÚ PACIENTES ---")
        print("a) Agregar paciente")
        print("b) Atender siguiente")
        print("c) Atender urgencia")
        print("d) Consultar posición")
        print("x) Salir")
        op = input("Opción: ").lower()

        if op == "a":
            nombre = input("Nombre paciente: ")
            lista.append(nombre)
        elif op == "b":
            if lista:
                print("Atendido:", lista.pop(0))
            else:
                print("Lista vacía.")
        elif op == "c":
            nombre = input("Nombre urgencia: ")
            lista.insert(0, nombre)
        elif op == "d":
            nombre = input("Nombre paciente: ")
            if nombre in lista:
                print("Faltan", lista.index(nombre), "para ser atendido.")
            else:
                print("No está en la lista.")
        elif op == "x":
            break

menu_pacientes()

#ejercicio 10#
import random

def crear_rodillos():
    return [
        ["X", "O", "7", "X", "O", "7", "X", "O", "7"],
        ["O", "7", "X", "O", "7", "X", "O", "7", "X"],
        ["7", "X", "O", "7", "X", "O", "7", "X", "O"]
    ]

def rotar(rodillo, n):
    return rodillo[n:] + rodillo[:n]

def tragamonedas():
    rodillos = crear_rodillos()
    while True:
        giros = [random.randint(0, 8) for _ in range(3)]
        r1 = rotar(rodillos[0], giros[0])
        r2 = rotar(rodillos[1], giros[1])
        r3 = rotar(rodillos[2], giros[2])
        print(f"Rodillos: {r1[0]} {r2[0]} {r3[0]}")

        if r1[0] == r2[0] == r3[0]:
            premio = {"X": 10, "O": 100, "7": 1000}[r1[0]]
            print(f"Ganó {premio} fichas!")
        else:
            print("Siga participando...")

        if input("¿Jugar otra vez? (s/n): ").lower() != "s":
            break

tragamonedas()
