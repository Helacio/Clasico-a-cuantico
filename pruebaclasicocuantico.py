import math
import clásicoacuántico as cac
resp = 0
test1 = print(cac.canicasbooleanas(1,[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,1,0,0],[0,0,0,1,0,0],[1,0,0,0,1,0]],[3,0,0,0,0,0]))
test2 = print(cac.sistemaprobabilistico([[2/3,1/3],[1/3,2/3]],[1,0],2))
test3 = print(cac.multiplesRendijascuantica([[1/math.sqrt(2),1J/math.sqrt(2)],[1/math.sqrt(2),-1j/math.sqrt(2)]],[1,0],2))
test4 = print(cac.grafica([1,2,6,4,8,1]))

if test1:
    resp =+ 1
if test2:
    resp += 1
if test3:
    resp += 1
if test4:
    resp += 1
print("Casos exitosos {} de 4".format(resp))

