import numpy as np

def modulocomplexnumber(number):
    return ((number.real**2)+(number.imag**2))**0.5

def sumavec(a, b):
    return np.add(a,b)

def inverso(a):
    d = [0 for i in range(len(a))]
    for i in range(len(a)):
        d[i] = -1 * a[i]
    return d

def escalarComplejo(n, b):
    for i in range(len(b)):
        b[i] = n * b[i]
    return b

def sumaMatricesComplejos(a, b):
    result = np.add(a,b)
    return result


def inversaDeUnaMatriz(a):
    m = []
    for i in range(len(a)):
        n = inverso(a[i])
        m.append(n)
    return m

def escalarPorComplejo(escalar, matriz):
    ctrl = len(matriz)
    ctrl2 = len(matriz[0])
    result = [[0 for i in range(ctrl2)] for j in range(len(matriz))]
    for i in range(ctrl):
        for j in range(ctrl2):
            result[i][j] = escalar * matriz[i][j]
    return result

def traspuesta(array):
    return np.transpose(array)

def conjugada(array):
    return np.conjugate(array)

def adjunta(array):
    return traspuesta(conjugada(array))

def producto_matrices(m, n):
    return np.matmul(m, n)

def accionmatrix(m, n):
    #m-> matriz n-> vector
    return np.matmul(m,n)

def productoInternoVectores(m,n):
    resultado = 0
    for i in range(len(m)):
        resultado += m[i] * n[i].conjugate()
    return resultado

def normaVector(m):
    return productoInternoVectores(m,m) ** 0.5

def distanceVectors(m,n):
    suma = 0
    for i in range(len(m)):
        suma += (m[i] - n[i]).real ** 2 + (m[i] - n[i]).imag ** 2
    return suma ** 0.5

def valuesAndVectosProp(matriz):
    valoresProp, vectoresProp = np.linalg.eig(matriz)
    return valoresProp, vectoresProp

def matrixunitaria(matriz):
    adj = adjunta(matriz)
    result = producto_matrices(adj, matriz)
    ctrl = len(result)
    cont = 0
    for i in range(ctrl):
        for j in range(ctrl):
            if i == j and result[i][j] == 1:
                cont +=1
    if cont == ctrl:
        return "Es unitaria"
    else:
        return "No es uniaria"

#print(matrixunitaria([[0,1j],[1j,0]]))

def hermitiana(matriz):
    ctrl = len(matriz)
    decide = ""
    for i in range(ctrl):
        for j in range(len(matriz[0])):
            if i != j and j > i:
                if matriz[i][j] == conjugada(matriz[j][i]):
                    continue
                else:
                    decide = None
    if decide == None:
        return "No es hermitiana"
    else:
        return"Es hermitiana"
#print(hermitiana([[0,1+2j],[1+2j,3]]))

def producTen(matrix1, matrix2):
    m = len(matrix1)
    mP = len(matrix1[0])
    n = len(matrix2)
    nP = len(matrix2[0])
    files = n*m
    columns = mP*nP
    result = [[0 for i in range(columns)] for j in range(files)]
    for j in range(files):
        for k in range(columns):
            result[j][k] += matrix1[j//n][k//nP] * matrix2[j % n][k%nP]
    return result
