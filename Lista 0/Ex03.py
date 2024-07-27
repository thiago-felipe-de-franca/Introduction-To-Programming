A = int(input())
L = int(input())
P = int(input())
H = int(input())
def maiorvalor(a,b):
    return (a + b + abs(a-b))/2

max_AL = maiorvalor(A, L)
max_LP = maiorvalor(L, P)
maior = maiorvalor(max_AL, max_LP)

M = maior * H

print(int(M))