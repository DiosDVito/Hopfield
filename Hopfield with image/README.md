# Red Hopfield

`hopfield2.py` implementa la red Hopfield para reconocer figuras de 7×7, con listas, `for`, `while` e `if`/`else`. No usa NumPy ni otras librerías.

La red guarda cinco iconos de videojuegos y, al recibir una figura con algunas celdas cambiadas, la corrige hasta llegar al icono guardado.

## Patrones

Cada archivo de `dataset/` es una matriz de 7×7 con solo `0` y `1`. Se lee por filas y cada `0` se cambia por `-1`. La red tiene 49 neuronas, una por celda.

| Archivo | Figura |
| --- | --- |
| `nave.txt` | nave |
| `invasor.txt` | invasor |
| `fantasma.txt` | fantasma |
| `hongo.txt` | hongo |
| `espada.txt` | espada |

## Qué hace el programa

1. Arma la matriz de pesos `T`. Cada peso es la suma de los productos entre neuronas de los patrones guardados. La diagonal queda en `0`, porque una neurona no se conecta consigo misma.
2. Copia cada figura y voltea cinco celdas: las cuatro esquinas y el centro. Donde había `0` pone `1`, y donde había `1` pone `0`. Esa copia es la consulta.
3. Toma la consulta como estado inicial `U`.
4. Calcula `U · T` y aplica la función `F`:
   - `1` si el resultado es positivo
   - `-1` si es negativo
   - el valor anterior si es `0`
5. Repite el paso 4 hasta que la figura ya no cambia. Todas las neuronas se actualizan a la vez.
6. Compara el resultado con los cinco iconos y escribe el nombre del que coincide.

## Consultas del ejemplo

Cada icono se prueba con las mismas cinco celdas cambiadas. En los cinco casos la red regresa a la figura guardada:

- la nave dañada vuelve a `nave`
- el invasor dañado vuelve a `invasor`
- el fantasma dañado vuelve a `fantasma`
- el hongo dañado vuelve a `hongo`
- la espada dañada vuelve a `espada`

## Ejecución

```text
python hopfield2.py
```

Primero imprime los patrones guardados. Cada bloque `Consulta` es la figura con celdas cambiadas. La flecha `->` muestra la figura ya estable, y `Figura reconocida` dice cuál icono es.
