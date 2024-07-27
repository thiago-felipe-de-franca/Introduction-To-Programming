entrada = int(input())


def mult_impar(n):
    if n == 1:
        return 1
    else:
        if n % 2 == 1:
            return n * mult_impar(n - 1)
        else:
            return 1 * mult_impar(n - 1)


x = mult_impar(entrada)
print(x)
