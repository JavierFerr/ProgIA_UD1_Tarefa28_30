# Unha xoguetería ten moito éxito en dous dos seus produtos: pallasos e bonecas.

# Adoita facer venda por correo e a empresa de loxística cóbralles por peso de cada paquete,
# así que deben calcular o peso dos pallasos e bonecas que sairán en cada paquete a demanda. Cada pallaso pesa 112 g e cada boneca 75 g.

# Escribir un programa que lea o número de pallasos e bonecas vendidos no último pedido e calcule o peso total en Kg do paquete que será enviado.

def venda(pallaso, boneca):
    total = pallaso * 112 + boneca * 75
    return total
    

if __name__ == '__main__':

    print("Introce numero de pallasos e de bonecas")
    pallaso, boneca = int(input()),int(input()) # type: ignore

    print(f"O peso do paquete é {venda(pallaso,boneca)} g ou {venda(pallaso,boneca)/1000} kg")
