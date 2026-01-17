# Mini-proyectos para practicar (principiante → intermedio)

Aquí tienes una colección de mini-proyectos pensados para practicar conceptos clave de Python. Cada proyecto incluye una breve descripción, objetivos, nivel y pistas.

- **Consejo**: intenta resolverlos primero sin mirar las soluciones; luego compara con `03-mini-proyectos-SOLUCIONES.py` si necesitas ayuda.

---

## 1) Calculadora de carrito de compra (Nivel: Principiante)
Objetivos:
- Practicar listas y diccionarios
- Uso de bucles, sum(), condicionales
Descripción:
Crea un pequeño programa que tenga una lista de productos (diccionarios con `name` y `price`). Calcula el subtotal, aplica IVA (por ejemplo 21%) y muestra el total.
Pistas:
- Usa `sum(p['price'] for p in products)`

---

## 2) Adivina el número (Nivel: Principiante)
Objetivos:
- Uso de `input()`, `random`, bucles y condicionales
Descripción:
Programa que elige un número aleatorio entre 1 y 100. El usuario intenta adivinar; el programa responde "más alto" o "más bajo" hasta que acierte.
Pistas:
- `import random` y `random.randint(1, 100)`

---

## 3) Gestor de tareas simple (To-Do) (Nivel: Principiante/Intermedio)
Objetivos:
- Manipular listas de diccionarios, funciones y persistencia simple (opcional)
Descripción:
Permite añadir, listar y eliminar tareas. Cada tarea es un diccionario `{"id": int, "title": str, "done": bool}`. Implementa un menú por consola.
Pistas:
- Genera `id` incrementales.

---

## 4) Analizador de texto (Nivel: Intermedio)
Objetivos:
- Strings, `split()`, `collections.Counter`, comprensión de listas
Descripción:
Lee una cadena (o un archivo) y calcula: número de palabras, palabras más frecuentes (top 5), y longitud media de palabra.
Pistas:
- `from collections import Counter`

---

## 5) Conversor de unidades (Nivel: Intermedio)
Objetivos:
- Funciones, mapeos (diccionarios), manejo de floats y formateo
Descripción:
Crea un conversor que transforme entre `km ↔ mi`, `C ↔ F`, y `kg ↔ lb`. Implementa una interfaz de consola que pida tipo de conversión y valores.
Pistas:
- Usa funciones separadas por conversión.

---

## 6) Generador de contraseñas (Nivel: Intermedio)
Objetivos:
- Uso de `random`, `string`, parámetros y validaciones
Descripción:
Genera contraseñas aleatorias con longitud variable y opciones para incluir mayúsculas, minúsculas, dígitos y símbolos.
Pistas:
- `import string` para `ascii_letters`, `digits`, `punctuation`

---

## 7) Mini-analítica de ventas (Nivel: Intermedio)
Objetivos:
- Listas, diccionarios, `sum`, `max`, `min`, `grouping`
Descripción:
Dada una lista de ventas con `{