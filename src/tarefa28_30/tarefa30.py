# Escribir unha función que calcule a área dun círculo e outra que calcule o volume dun cilindro usando a primeira función.
# É dicir, o volume do cilindro é a área do circulo que forma a base pola altura do cilibro.
# Polo que dende dentro da función para calcular o volume do cilindro hai que chamar á función que calcula a área do circulo que forma a base.

#    A area do círculo é pi*r**2
#    O volume do cilindro é pi*r**2 * h

# Nota: O valor de PI o tes dentro dó módulo math.

# import math

# print(math.pi)

import math

def areaCir(r):
    return math.pi * r**2

def volumCil(r,h):
    return areaCir(r)* h

if __name__ == '__main__':

    print("Introduzca o radio e altura do cilindro (cm)")
    r,h = float(input()),float(input())
    print(f"O volume e de {volumCil(r,h)} cm2")