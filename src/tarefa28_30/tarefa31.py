# Escribir un programa que almacene as materias dun curso (por exemplo Matemáticas, Física, Química, Historia e Lingua)
# nunha lista e a mostre por pantalla coa mensaxe Eu estudo <materia>,
# onde <materia> é cada unha das materias da lista.

def estudo(materias):
    for materia in materias:
        print(f"Eu estudo {materia}")
    

if __name__ == '__main__':

    materias = ["Matemáticas", "Física", "Química", "Historia", "Lingua"]

    estudo(materias)
    
