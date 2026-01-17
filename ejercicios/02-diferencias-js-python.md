# Diferencias Clave: JavaScript vs Python

Guía rápida para programadores JavaScript que aprenden Python.

## 📌 Sintaxis Básica

### Variables

```javascript
// JavaScript
const nombre = "Sofi";
let edad = 25;
var ciudad = "Madrid"; // evitar var
```

```python
# Python - No necesitas const/let/var
nombre = "Sofi"
edad = 25
ciudad = "Madrid"
```

### Constantes

```javascript
// JavaScript
const PI = 3.14159;
```

```python
# Python - Convención: MAYÚSCULAS (pero no es inmutable)
PI = 3.14159
```

---

## 🔤 Strings

### Template Literals vs f-strings

```javascript
// JavaScript
const nombre = "Sofi";
const saludo = `Hola ${nombre}!`;
```

```python
# Python - f-strings (Python 3.6+)
nombre = "Sofi"
saludo = f"Hola {nombre}!"
```

### Métodos comunes

```javascript
// JavaScript
str.toUpperCase()
str.toLowerCase()
str.includes("texto")
str.split(" ")
```

```python
# Python
str.upper()
str.lower()
"texto" in str  # En lugar de includes
str.split(" ")
```

---

## 📚 Arrays vs Listas

```javascript
// JavaScript
const frutas = ["manzana", "banana", "naranja"];
frutas.push("uva");           // Agregar al final
frutas.unshift("fresa");      // Agregar al inicio
frutas.pop();                 // Eliminar último
frutas.shift();               // Eliminar primero
```

```python
# Python
frutas = ["manzana", "banana", "naranja"]
frutas.append("uva")          # Agregar al final
frutas.insert(0, "fresa")     # Agregar al inicio
frutas.pop()                  # Eliminar último
frutas.pop(0)                 # Eliminar primero
```

---

## 📦 Objetos vs Diccionarios

```javascript
// JavaScript
const usuario = {
  nombre: "Sofi",
  edad: 25,
  activo: true
};

console.log(usuario.nombre);      // Notación punto
console.log(usuario["nombre"]);   // Notación corchetes
```

```python
# Python - Diccionarios
usuario = {
    "nombre": "Sofi",
    "edad": 25,
    "activo": True  # True con mayúscula
}

print(usuario["nombre"])    # Solo notación corchetes
print(usuario.get("nombre")) # Método alternativo seguro
```

---

## 🔁 Loops

### For Loop

```javascript
// JavaScript - Iterar números
for (let i = 0; i < 5; i++) {
  console.log(i);
}

// Iterar array
frutas.forEach(fruta => console.log(fruta));

// For...of
for (const fruta of frutas) {
  console.log(fruta);
}
```

```python
# Python - Iterar números
for i in range(5):  # 0 a 4
    print(i)

for i in range(1, 6):  # 1 a 5
    print(i)

# Iterar lista
for fruta in frutas:
    print(fruta)

# Con índice (como enumerate)
for index, fruta in enumerate(frutas):
    print(f"{index}: {fruta}")
```

### While Loop

```javascript
// JavaScript
let i = 0;
while (i < 5) {
  console.log(i);
  i++;
}
```

```python
# Python
i = 0
while i < 5:
    print(i)
    i += 1  # No existe i++ en Python
```

---

## ⚡ Funciones

### Declaración básica

```javascript
// JavaScript
function sumar(a, b) {
  return a + b;
}

// Arrow function
const sumar = (a, b) => a + b;
```

```python
# Python - Solo una forma
def sumar(a, b):
    return a + b
```

### Parámetros por defecto

```javascript
// JavaScript
function saludar(nombre = "Usuario") {
  return `Hola ${nombre}`;
}
```

```python
# Python
def saludar(nombre="Usuario"):
    return f"Hola {nombre}"
```

---

## 🎯 Condicionales

### If/Else

```javascript
// JavaScript
if (edad >= 18) {
  console.log("Adulto");
} else if (edad >= 13) {
  console.log("Adolescente");
} else {
  console.log("Niño");
}
```

```python
# Python - No llaves, usa indentación
if edad >= 18:
    print("Adulto")
elif edad >= 13:  # elif en lugar de else if
    print("Adolescente")
else:
    print("Niño")
```

### Operador ternario

```javascript
// JavaScript
const resultado = edad >= 18 ? "Adulto" : "Menor";
```

```python
# Python
resultado = "Adulto" if edad >= 18 else "Menor"
```

---

## ✨ Características Especiales

### Array Methods vs List Comprehensions

```javascript
// JavaScript - map
const cuadrados = [1, 2, 3, 4, 5].map(x => x ** 2);

// filter
const pares = [1, 2, 3, 4, 5].filter(x => x % 2 === 0);
```

```python
# Python - List comprehension (más idiomático)
cuadrados = [x ** 2 for x in [1, 2, 3, 4, 5]]

pares = [x for x in [1, 2, 3, 4, 5] if x % 2 == 0]

# También existen map() y filter() pero son menos usados
cuadrados = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
```

### Destructuring

```javascript
// JavaScript
const [primero, segundo, ...resto] = [1, 2, 3, 4, 5];
const {nombre, edad} = usuario;
```

```python
# Python - Unpacking
primero, segundo, *resto = [1, 2, 3, 4, 5]
# No hay destructuring de diccionarios directamente
```

---

## 🚨 Valores Falsy

```javascript
// JavaScript - Falsy values
false, 0, "", null, undefined, NaN
```

```python
# Python - Falsy values
False, 0, "", None, [], {}, ()
# No existe undefined ni NaN (es float('nan'))
```

---

## 🔢 Comparaciones

```javascript
// JavaScript
=== // Igualdad estricta
!== // Desigualdad estricta
==  // Igualdad con coerción (evitar)
```

```python
# Python
== # Igualdad (siempre estricta, no hay coerción)
!= # Desigualdad
is # Identidad de objeto (como === para objetos)
```

---

## 📝 Convenciones de Nombres

```javascript
// JavaScript - camelCase
const nombreCompleto = "Sofi Dev";
function calcularTotal() {}
```

```python
# Python - snake_case
nombre_completo = "Sofi Dev"
def calcular_total():
    pass

# Clases en PascalCase (igual que JS)
class UsuarioActivo:
    pass
```

---

## 💡 Consejos para la Transición

1. **Indentación**: Python usa indentación obligatoria (4 espacios recomendados)
2. **No semicolons**: No necesitas `;` al final de las líneas
3. **No llaves**: Usa `:` e indentación en lugar de `{}`
4. **Booleanos**: `True` y `False` con mayúscula inicial
5. **None**: Equivalente a `null` en JavaScript
6. **Print**: `print()` en lugar de `console.log()`
7. **Type hints** (opcional): Python 3.5+ soporta anotaciones de tipo

```python
# Type hints (opcional pero útil)
def sumar(a: int, b: int) -> int:
    return a + b
```

---

## 🎓 Recursos Adicionales

- [Python para programadores JS](https://www.pythonforbeginners.com/basics/python-for-javascript-developers)
- [Documentación oficial de Python](https://docs.python.org/es/3/tutorial/)
- [Real Python - Coming from JavaScript](https://realpython.com/python-for-javascript-developers/)
