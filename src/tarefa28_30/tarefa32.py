# Escribir un programa que almacene as materias dun curso (por exemplo Matemáticas, Física, Química, Historia e Lingua) nunha lista,
# pregunte ao usuario a nota que sacou en cada materia, e despois as amose por pantalla coa mensaxe
# En sacaches un onde é cada unha das materias da lista e cada unha das correspondentes notas introducidas polo usuario.

def boletin (notas):
    for clave in notas.keys():
        print(f"{clave} {notas[clave]}")


if __name__ == '__main__':

    notas = {}

    materias = ["Matemáticas", "Física", "Química", "Historia", "Lingua"]
    for materia in materias:
        print(f"Introduce a nota de {materia}")
        notas[materia] = input()

        
    print("\nBoletín de notas \n")
    boletin(notas)
    print("\n")