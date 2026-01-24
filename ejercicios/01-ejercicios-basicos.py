"""
EJERCICIOS BÁSICOS DE PYTHON
Para principiantes con experiencia en JavaScript

Instrucciones: Completa cada ejercicio. Puedes ejecutar el archivo completo
o comentar los ejercicios que no estés trabajando.
"""

# =============================================================================
# EJERCICIO 1: Variables y tipos de datos
# =============================================================================
# En JavaScript usarías: const greeting = `Hola ${name}`;
# En Python, crea una variable con tu nombre y otra con tu edad
# Luego imprime: "Me llamo [nombre] y tengo [edad] años"

# Tu código aquí:

# name = "Sofi"
# age = 18
# message =  f'Hello my name is  {name} and I am {age} years old'
# print(message)

# =============================================================================
# EJERCICIO 2: Listas (similar a arrays en JS)
# =============================================================================
# Crea una lista con tus 5 lenguajes de programación favoritos
# Imprime el primer y último elemento
# Agrega un nuevo lenguaje al final usando .append()

# Tu código aquí:

# favoriteLanguajes = ['javascript🦨','javascript','javascript2🦝']


# print(favoriteLanguajes[0],favoriteLanguajes[2])
# favoriteLanguajes.append('javascript💖')
# print(favoriteLanguajes)

# =============================================================================
# EJERCICIO 3: Diccionarios (similar a objetos en JS)
# =============================================================================
# En JavaScript: const user = { name: 'Sofi', age: 25, isActive: true };
# Crea un diccionario llamado "producto" con:
# - nombre (str)
# - precio (float)
# - en_stock (bool)
# - categorias (list)

# Tu código aquí:
# product = {
#  "name": "Sabritas",
#  "price": 10.5,
#  "in_stock": True,
#  "categories": ["comida mala", "comida alta ern calorías", "paitas" ]
# }

# print(product)


# =============================================================================
# EJERCICIO 4: Condicionales
# =============================================================================
# Crea una variable "temperatura" con un número
# Si es mayor a 30, imprime "Hace calor"
# Si está entre 15 y 30, imprime "Clima agradable"
# Si es menor a 15, imprime "Hace frío"

# Tu código aquí:
# temperature = 40

# if temperature > 30:
#     print("Hace calor🥵")
# elif temperature >= 15:
#     print("Clima meh 🦨💨")
# else:
#     print("Hace Frío🥶")





# =============================================================================
# EJERCICIO 5: Bucles - for con range
# =============================================================================
# En JavaScript: for(let i = 1; i <= 10; i++) { console.log(i); }
# En Python, usa range() para imprimir números del 1 al 10

# Tu código aquí:

# for i in range(1,11):
#     print(i)

# =============================================================================
# EJERCICIO 6: Bucles - for con listas
# =============================================================================
# En JavaScript: frutas.forEach(fruta => console.log(fruta));
# Crea una lista de frutas e imprime cada una usando un for loop

# Tu código aquí:

# fruits = ['apple 🍎', 'banana🍌', 'pineapple 🍍' ]
# for x in fruits:
#     print(x)


# ==============================================================================
# EJERCICIO 7: Funciones básicas
# =============================================================================
# En JavaScript: function saludar(nombre) { return `Hola ${nombre}`; }
# Crea una función que reciba un nombre y retorne un saludo personalizado

# Tu código aquí:

# def greeting(name):
#     print(f'Hi {name}')

# greeting('Sofia')

# =============================================================================
# EJERCICIO 8: Funciones con múltiples parámetros
# =============================================================================
# Crea una función "calcular_promedio" que reciba tres números
# y retorne el promedio de los tres

# Tu código aquí:


# def calc__average(*args):
#     total = 0
#     for x in args:
#         total += x

#     return total /  len(args)

# result = calc__average(3,4,1)

# print(result)

# =============================================================================
# EJERCICIO 9: Trabajando con strings
# =============================================================================
# Crea una variable con tu frase favorita
# Conviértela a mayúsculas, minúsculas y cuenta cuántas palabras tiene
# Pista: usa .upper(), .lower() y .split()

# Tu código aquí:

# favorite_word = 'Patata Frita'

# word_upper = favorite_word.upper()
# word_lower = favorite_word.lower()
# word_count = favorite_word.split()
# counted_words = len(word_count)
# print(word_upper)
# print(word_lower)
# print(counted_words)

# =============================================================================
# EJERCICIO 10: List comprehension (más avanzado)
# =============================================================================
# En JavaScript: const cuadrados = [1,2,3,4,5].map(x => x ** 2);
# Crea una lista con los cuadrados de los números del 1 al 10
# usando list comprehension: [expresion for item in iterable]

# Tu código aquí:

# cuadrados = [i** 2 for i in range(1,11)]
# print(cuadrados)


# =============================================================================
# EJERCICIO BONUS: Mini proyecto
# =============================================================================
# Crea un programa que:
# 1.[x] Tenga una lista de productos con sus precios (diccionarios)
# 2.[x] Calcule el total de todos los productos
# 3.[] Aplique un descuento del 10% si el total es mayor a 100
# 4.[] Imprima el total final

# Tu código aquí:

products = [
    {"name": "Laptop", "price": 750.0, "in_stock": True, "categories": ["electrónica", "computación"]},
    {"name": "Auriculares", "price": 50.0, "in_stock": True, "categories": ["electrónica", "audio"]},
    {"name": "Camiseta", "price": 20.0, "in_stock": False, "categories": ["ropa"]},
    {"name": "Libreta", "price": 8.5, "in_stock": True, "categories": ["papelería"]},
    {"name": "Mochila", "price": 35.0, "in_stock": True, "categories": ["accesorios", "viaje"]},
]

def total_products(prod):
    total = 0
    for product in prod:
       total += product['price']
    return total

result = total_products(products)
print(result)

discounted_total= 0
if result > 100:
    discounted_total = result * .9

print(result)
print( discounted_total)