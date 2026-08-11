"""
Módulo: 01 - Sintaxis y Semántica
Roadmap: Fundamentos de Programación 
Descripción: Notas y ejemplos prácticos sobre las reglas de sintaxis y errores semánticos en Python.
Theory Notes: notes/programming-fundamentals/01_syntax_and_semantics.md
"""


# 1. SINTAXIS (La gramática del lenguaje)

# La sintaxis son las reglas estrictas de estructura. Si falla, Python da SyntaxError.

# A) Indentación: Define qué bloques de código están dentro de qué estructuras.
if 5 > 3:
    print("Cinco es mayor que tres")  # Está dentro de la condición
print("Como este print está fuera de la indentación, es independiente de la condición")

# B) Uso de dos puntos (:): Obligatorios al definir funciones, condicionales, bucles, etc.
def validacion(age):
    if age >= 18:
        print("Puede pasar")

# C) Palabras reservadas: No se pueden usar como nombres de variables.
# class = "math"  # <--- Si se descomenta, da SyntaxError porque 'class' es una palabra reservada.



# 2. SEMÁNTICA (El significado / La lógica)

# El código está bien escrito (sin errores de sintaxis) y ejecuta,
# pero el resultado es INCORRECTO porque la lógica falló.

# Ejemplo: Queremos calcular el promedio de dos notas (10 y 20).
# Promedio esperado = (10 + 20) / 2 = 15.0

nota1 = 10
nota2 = 20

# ERROR SEMÁNTICO: Olvidamos los paréntesis y Python aplica prioridad de operaciones.
# Hace primero 20 / 2 = 10, y luego 10 + 10 = 20.0 (El código corre, pero el resultado está mal).
promedio_incorrecto = nota1 + nota2 / 2
print("Promedio con error semántico:", promedio_incorrecto)

# FORMA CORRECTA (Semántica corregida):
promedio_correcto = (nota1 + nota2) / 2
print("Promedio correcto:", promedio_correcto)