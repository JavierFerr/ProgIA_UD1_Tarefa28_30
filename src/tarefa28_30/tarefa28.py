# Escribir unha función que calcule o total dunha factura tras aplicarlle o IVE. A función debe recibir a cantidade sen IVE e a porcentaxe de IVE a aplicar,
# e devolver o total da factura.

# Se se invoca a función sen pasarlle a porcentaxe de IVE, deberá aplicar un 21%.

def total(base, porcentaxe = 21):
    return base + (base * porcentaxe / 100)

if __name__ == '__main__':

    print("Introduzca o valor sen IVE e o porcentaxe de IVE (Enter para aplicar o 21%)")
    base = float(input())
    porcentaxe_input = input()
    porcentaxe = float(porcentaxe_input) if porcentaxe_input else 21
    print(f"{total(base,porcentaxe)} €")