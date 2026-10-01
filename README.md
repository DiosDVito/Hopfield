# Red Hopfield

`hopfield.py` implementa la red Hopfield del ejemplo, con listas, `for`, `while` e `if`/`else`. No usa NumPy ni otras librerías.

La red guarda dos patrones de 2×2 y, al recibir un vector, lo va corrigiendo hasta llegar al patrón guardado más parecido.

## Patrones

Se leen por filas y cada `0` se cambia por `-1`:

| Matriz | Vector |
| --- | --- |
| `1 1` / `1 0` | `(1, 1, 1, -1)` |
| `0 0` / `0 1` | `(-1, -1, -1, 1)` |

## Qué hace el programa

1. Arma la matriz de pesos `T`. Cada peso es la suma de los productos entre neuronas de los patrones guardados. La diagonal queda en `0`, porque una neurona no se conecta consigo misma.
2. Toma una consulta `A` como estado inicial `U`.
3. Calcula `U · T` y aplica la función `F`:
   - `1` si el resultado es positivo
   - `-1` si es negativo
   - el valor anterior si es `0`
4. Repite el paso 3 hasta que el vector ya no cambia.

## Consultas del ejemplo

- `(1, 1, 1, -1)` ya es el primer patrón, así que no cambia.
- `(-1, -1, -1, -1)` pasa a `(-1, -1, -1, 1)`, el segundo patrón, y ahí se detiene.

## Ejecución

```text
python hopfield.py
```

Cada línea `A = ...` es la consulta. La flecha `->` muestra el vector antes y después de un paso. Cuando ambos lados son iguales, la red ya está estable.
