# Red Hopfield del ejemplo (patrones de 2 x 2).
# Solo listas, for, while e if/else.

n = 4
x = [
    [1, 1, 1, 0],
    [0, 0, 0, 1]
]
consultas = [
    [1, 1, 1, -1],
    [-1, -1, -1, -1]
]

for k in range(2):
    for i in range(n):
        if x[k][i] == 0:
            x[k][i] = -1

T = []
for i in range(n):
    fila = []
    for j in range(n):
        fila.append(0)
    T.append(fila)

for k in range(2):
    for i in range(n):
        for j in range(n):
            if i != j:
                T[i][j] = T[i][j] + x[k][i] * x[k][j]

print("Patrones:", x)
print("T:")
for i in range(n):
    print(T[i])

for c in range(2):
    U = []
    for i in range(n):
        U.append(consultas[c][i])
    print("A =", U)

    estable = 0
    while estable == 0:
        siguiente = []
        for j in range(n):
            suma = 0
            for i in range(n):
                suma = suma + U[i] * T[i][j]
            if suma > 0:
                siguiente.append(1)
            else:
                if suma < 0:
                    siguiente.append(-1)
                else:
                    siguiente.append(U[j])
        print(" ", U, "->", siguiente)
        estable = 1
        for j in range(n):
            if siguiente[j] != U[j]:
                estable = 0
            U[j] = siguiente[j]
