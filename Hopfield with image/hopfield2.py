#Daniel Esparza Arizpe - A01637076
#Hopfield with image Activity

import os


def leer_figura(ruta):
    figura = []
    with open(ruta, "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea != "":
                fila = []
                partes = linea.split()
                for p in partes:
                    fila.append(int(p))
                figura.append(fila)
    return figura


def a_vector(figura):
    vector = []
    for i in range(len(figura)):
        for j in range(len(figura[i])):
            if figura[i][j] == 0:
                vector.append(-1)
            else:
                vector.append(1)
    return vector


def imprimir(vector, filas, columnas):
    indice = 0
    for i in range(filas):
        texto = ""
        for j in range(columnas):
            if vector[indice] == 1:
                texto = texto + "1 "
            else:
                texto = texto + "0 "
            indice = indice + 1
        print(texto)


def entrenar(patrones):
    n = len(patrones[0])
    T = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(0)
        T.append(fila)
    for k in range(len(patrones)):
        for i in range(n):
            for j in range(n):
                if i != j:
                    T[i][j] = T[i][j] + patrones[k][i] * patrones[k][j]
    return T


def revolver(figura, cambios):
    consulta = []
    for i in range(len(figura)):
        fila = []
        for j in range(len(figura[i])):
            fila.append(figura[i][j])
        consulta.append(fila)
    for c in range(len(cambios)):
        i = cambios[c][0]
        j = cambios[c][1]
        if consulta[i][j] == 0:
            consulta[i][j] = 1
        else:
            consulta[i][j] = 0
    return consulta


def recuperar(U, T):
    estado = []
    for valor in U:
        estado.append(valor)
    n = len(estado)
    iteracion = 0
    estable = 0
    while estable == 0 and iteracion < 100:
        siguiente = []
        for j in range(n):
            suma = 0
            for i in range(n):
                suma = suma + estado[i] * T[i][j]
            if suma > 0:
                siguiente.append(1)
            else:
                if suma < 0:
                    siguiente.append(-1)
                else:
                    siguiente.append(estado[j])
        estable = 1
        for j in range(n):
            if siguiente[j] != estado[j]:
                estable = 0
            estado[j] = siguiente[j]
        iteracion = iteracion + 1
    return estado


def reconocer(U, patrones, nombres):
    for k in range(len(nombres)):
        igual = 1
        for i in range(len(U)):
            if U[i] != patrones[k][i]:
                igual = 0
        if igual == 1:
            return nombres[k]
    return "ninguna"


if __name__ == "__main__":
    carpeta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dataset")
    nombres = ["nave", "invasor", "fantasma", "hongo", "espada"]
    cambios = [[0, 0], [0, 6], [6, 0], [6, 6], [3, 3]]

    figuras = []
    for nombre in nombres:
        figuras.append(leer_figura(os.path.join(carpeta, nombre + ".txt")))

    filas = len(figuras[0])
    columnas = len(figuras[0][0])

    patrones = []
    for figura in figuras:
        patrones.append(a_vector(figura))

    T = entrenar(patrones)

    print("Patrones guardados")
    for k in range(len(nombres)):
        print(nombres[k])
        imprimir(patrones[k], filas, columnas)

    for k in range(len(nombres)):
        consulta = a_vector(revolver(figuras[k], cambios))
        print("Consulta")
        imprimir(consulta, filas, columnas)
        estable = recuperar(consulta, T)
        print("->")
        imprimir(estable, filas, columnas)
        print("Figura reconocida:", reconocer(estable, patrones, nombres))
