def polinomial(x, a, b, c, d, e):
    return a * (x + b) ** c + (e * x) + d


def derivada(x, h, a, b, c, d, e):
    return (polinomial(x + h, a, b, c, d, e) - polinomial(x, a, b, c, d, e)) / h


def equacao_reta_tangente(x, y, derivada_resultado):
    termo_independente = y - (derivada_resultado * x)
    return derivada_resultado, termo_independente


def formatar_equacao_reta(derivada_resultado, termo_independente):
    equacao = f"y={round(derivada_resultado, 3)}*x"
    if round(termo_independente, 3) != 0:
        equacao += f"{'' if termo_independente < 0 else '+'}{round(termo_independente, 3)}"
    return equacao


def encontrar_raiz(x1, a, b, c, d, e):
    x = x1
    y1 = polinomial(x, a, b, c, d, e)
    while True:
        if round(y1, 3) == 0.0:
            return x, y1
        elif round(a, 3) == 0 and round(e * x, 3) == 0:
            print(f"Maldição, a função é aproximadamente a reta y={round(d, 3)} que é paralela ao eixo das abscissas, não tem raiz e não é possível aplicar o método.")
            return
        else:
            derivada_resultado = derivada(x, 1e-9, a, b, c, d, e)
            if round(derivada_resultado, 3) == 0:
                print(f"Encontramos o ponto ({round(x, 3)};{round(y1, 3)}) da função, a equação da reta tangente deste ponto é aproximadamente y={round(y1, 3)}, porém, ainda não é a raiz devemos continuar para otimizar a trajetória do disparo.")
                print(f"Droga, a reta tangente y={round(y1, 3)} é paralela ao eixo das abscissas, não tem raiz, tenho pena de quem estiver usando a arma quando isto acontecer, kkkkk.")
                return
            else:
                k, p = equacao_reta_tangente(x, y1, derivada_resultado)
                equacao_reta = formatar_equacao_reta(k, p)
                print(f"Encontramos o ponto ({round(x, 3)};{round(y1, 3)}) da função, a equação da reta tangente deste ponto é aproximadamente {equacao_reta}, porém, ainda não é a raiz devemos continuar para otimizar a trajetória do disparo.")
                x = -p / k
                y1 = polinomial(x, a, b, c, d, e)
                if round(y1, 3) == 0.0:
                    print(f"Acertou em cheio! A raiz foi encontrada e o valor dela nas abscissas é aproximadamente {round(x, 3)}, e a equação da reta tangente neste ponto é aproximadamente {equacao_reta}.")
                    return


x1 = float(input())
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())

encontrar_raiz(x1, a, b, c, d, e)
