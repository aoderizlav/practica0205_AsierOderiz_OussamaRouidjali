lista = ["SIPA", "DAPI", "SIRC", "GPIT"]
nota = []
for asignatura in lista:
    print("Introduzca su nota de asignatura", asignatura)
    nota.append(input())

for asignatura in range(len(lista)):
    print(lista[asignatura], ":", nota[asignatura], sep="")
