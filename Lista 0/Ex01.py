D = int(input())
# print ('Tantan deseja', D, 'diamantes')
# Arthur -> 10
# Luiz -> 30
# Pedro -> 100
if (D <= 10):
    print('Arthur')
elif D <= 30:
    print('Luiz')
elif D <= 100:
    print('Pedro')
else:
    print('Nenhum')