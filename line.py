import math

def line():
    coA = float(input("Ingrese el coeficiente A: "))
    coB = float(input("Ingrese el coeficiente B: "))
    coX1 = float(input("Ingrese el coeficiente X1: "))
    coX2 = float(input("Ingrese el coeficiente X2: "))
    coY1 = (coA * coX1) + coB
    coY2 = (coA * coX2) + coB

    coX3 = coX1
    coY3 = coY2

    dist = math.sqrt(((coX2 - coX3)**2) + ((coY1 - coY3)**2))

    print(f"El coeficiente A de su ecuacion de la recta es: {coA}")
    print(f"El coeficiente B de su ecuacion de la recta es: {coB}")
    print(f"El coeficiente X1 de su ecuacion de la recta es: {coX1}")
    print(f"El coeficiente X2 de su ecuacion de la recta es: {coX2}")

    print("\nPara la siguiente ecuacion:")
    print(f"\t Y = {coA}X + {coB}")

    print("\nDados los siguientes puntos:")
    print(f"\tP1 ({coX1}, {coY1})")
    print(f"\tP1 ({coX2}, {coY2})") 

    print(f"\nLa distancia entre ellos es: {dist}")

line()