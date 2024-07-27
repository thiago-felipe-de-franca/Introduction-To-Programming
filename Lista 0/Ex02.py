# Hogsmeade (X: 34, Y: 110, Z: 220)
# Kakariko (X: 0, Y: 64, Z: 0)
# Solitude (X: 140, Y: 200, Z: 456)

import math

X = int(input())
Z = int(input())

H = math.sqrt((34 - X)**2 + (220 - Z)**2)
K = math.sqrt((0 - X)**2 + (0 - Z)**2)
S = math.sqrt((140 - X)**2 + (456 - Z)**2)

H = format(H, ".2f")
K = format(K, ".2f")
S = format(S, ".2f")

print("Distancia para Hogsmeade:", H)
print("Distancia para Kakariko:", K)
print("Distancia para Solitude:", S)