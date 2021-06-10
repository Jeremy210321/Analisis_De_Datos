print("\t\t\t\t---MULTIPLICACIÓN DE MATRICES--")
print("\n")
filasA = int(input("ingresa el numero de filas de la PRIMERA matriz: "))
filasB = int(input("ingresa el numero de filas de la SEGUNDA matriz: "))
columnasA = int(input("ingresa el numero de columnas de la PRIMERA matriz: "))
columnasB = int(input("Ingresa el numero de columnas de la SEGUNDA matriz: "))
matrizR = [] #Matriz resultante
# Creacion de la primera Matriz
print(" ")
print("\t\t--- Primera Matríz -------")
print(" ")
matrizA = []
for i in range(filasA):
    matrizA.append([0] * columnasA)
    print(matrizA[i])
# Creacion de la segunda Matríz
print(" ")
print("\t\t--- Segunda Matriz ---")
print(" ")
M2 = []
for i in range(columnasA):
    M2.append([0] * columnasB)
    print(M2[i])
if columnasA != filasB:
    print("No se puede multiplicar estas matrices")
else:
    print(" ")
    print("Ingresa los valores de la primera matriz 1")
    print(" ")

    # Intercambio de valores en la primera matriz 1
    for i in range(filasA):
        for j in range(columnasA):
            matrizA[i][j] = int(float(input("Introduce los valores en (%d, %d): " % (i, j))))
    print(" ")
    print("\t--- Valores ingresados en la primera matriz")
    print(" ")
    for i in range(filasA):
        print(matrizA[i])

    print(" ")
    print("Ingresa los valores de la primera matriz  2")
    print(" ")
    # Intercambio de valores en la primera matriz 2

    for i in range(columnasA):
        for j in range(columnasB):
            M2[i][j] = int(float(input("Ingrese los valores en (%d,%d) : " % (i, j))))
    print(" ")
    print("\t--- Valores ingresados en la segund matriz -------")
    print(" ")
    for i in range(columnasA):
        print(M2[i])
    print(" ")
    print("\t\t\t----- MULTIPLICACIÓN -----")
    print(" ")
    # Matriz de resultado

    for i in range(filasB):
        matrizR.append([0] * columnasB)

    # MULTIPLICACION
    for i in range(filasA):
        for j in range(columnasA):
            for k in range(columnasB):
                matrizR[i][k] = matrizR[i][k]+(matrizA[i][j]*M2[j][k])

    for i in range(filasA):
        M = []
        for j in range(columnasB):
            M.append(matrizR[i][j])
        print(M)
