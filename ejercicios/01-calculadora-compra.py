## 1) Calculadora de carrito de compra (Nivel: Principiante)
# Objetivos:
# - Practicar listas y diccionarios
# - Uso de bucles, sum(), condicionales
# Descripción:
#  [x] Crea un pequeño programa que tenga una lista de productos (diccionarios con `name` y `price`).
# []Calcula el subtotal
# [] aplica IVA (por ejemplo 16%)
# [] muestra el total.
# Pistas:
# - Usa `sum(p['price'] for p in products)`

products = [
    {'name': 'Laptop', 'price': 800.00},
    {'name': 'Mouse', 'price': 25.50},
    {'name': 'Teclado', 'price': 45.00},
    {'name': 'Monitor', 'price': 300.00},
    {'name': 'Auriculares', 'price': 60.00}
]

subtotal = sum(p['price'] for p in products)
print(f'El sub total es {subtotal}')

total =  subtotal / 1.16
print(f'El total con IVA es: {total}')
