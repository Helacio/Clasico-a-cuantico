import complejos as cp
import numpy as np
import matplotlib.pyplot as mplt

#1. CANICAS CON COEFICIENTES BOOLEANOS...
def canicasbooleanas(clicks, booleanMatrix, estadoInicial):
    if clicks >= 0 and type(clicks) is int:
        for i in range(len(booleanMatrix)):
            for j in range(len(booleanMatrix[0])):
                if booleanMatrix[i][j] == 0 or booleanMatrix[i][j]==1:
                    continue
                else:
                    return "Verifique el estado Booleano de la matriz"
        for c in range(clicks):
            estadoInicial = cp.accionmatrix(booleanMatrix, estadoInicial)
        return estadoInicial



#2. MÚLTIPLES RENDIJAS CLÁSICO PROBABILÍSTICO...
def sistemaprobabilistico(matrix, estadoInicial, clicks):
    if (clicks >= 0) and (type(clicks) is int):
        length = len(matrix)
        lenght2 = len(matrix[0])
        for i in range(length):
            for j in range(lenght2):
                if matrix[i][j] == 0 or type(matrix[i][j]) is float:
                    continue
                else:
                    return "Verifique el estado probabilístico"
        for x in range(clicks):
            estadoInicial = cp.accionmatrix(matrix, estadoInicial)
        return estadoInicial


#2.1 INTERFÁZ MULTIPLES RENDIJAS
def multiplerendijaclasico(matrix, vectIni, clicks):
    return sistemaprobabilistico(matrix, vectIni, clicks)

#3. MÚLTIPLES RENDIJAS CUÁNTICO
def multiplesRendijascuantica(matriz, estadoinic, clicks):
    matriz_transpuesta = cp.traspuesta(matriz)
    for i in range(len(matriz_transpuesta)):
        if int(sum(matriz_transpuesta[i])) != 1:
            return "Verifique que la matriz sea unitaria"
        else:
            for i in range(clicks):
                resp = cp.accionmatrix(matriz,estadoinic)
        return resp


#4. GRÁFICA:
#Solo se recibe vectores dado que es el resultado obtenido de los puntos anteriores.
def grafica(vector):
    lenght = len(vector)
    x = np.array([x for x in range(lenght)])
    y = np.array(vector)
    mplt.bar(x,y)
    mplt.xlabel("Posición")
    mplt.ylabel("Probabilidad")
    mplt.show()
