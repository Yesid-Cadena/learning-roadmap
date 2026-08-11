Tema: Syntaxis y semantica
**Fecha:** 2026-08-11

Método de Aprendizaje:
Este apartado de notas busca hacer el ejercicio de pensar realmente el concepto y explicarlo con mis propias palabras, no solo copiar y pegar texto sin finalidad.



Syntaxis = Según entiendo la Syntaxis es la manera correcta de escribir en un lenguage de programación para que este pueda ser interpretado de manera correcta.
Son las reglas de la escritura en un lenguage determinado.
En este sentido, en caso de que se cometa algun error de syntaxis el programa no va a compilar y me retornara un error.

**Consecuencia de error:** En caso de cometer un error sintáctico, el programa no podrá ejecutarse/interpretarse y nos retornará un error directo (ej. `SyntaxError`).



Semantica = Según entiendo la semantica se refiere en un sentido más logico, que hace cada instrucción al ejecutarse, que valores toman, como se comportan los tipos de datos, etc.

**Consecuencia de error:** El código se ejecuta de forma efectiva (no rompe al inicio), pero produce un resultado incorrecto o no cumple fielmente con su propósito.

Ejemplos y Explicación Lógica

'''python
# Ejemplo
edad = int(input("Ingrese su edad para evaluar si es mayor de edad"))
if edad > 18:
    print("Usted es mayor de edad")'''

Explicación: Este codigo tiene un error semántico, aunque se compila sin errores, no cumple fielmente con su proposito: si la persona tiene 18 años efectivamente es mayor de edad, pero este mensaje nunca sera impreso ya que falto el sigo "="

'''python
# Ejemplo
edad = "5" ----> se toma como un String
print(10 + edad)
'''
Explicación: No siempre pasa que se ejecuta, en este caso nos da un error por un tema de incompatibilidad en los tipos de datos, es sintacticamente correcta pero no semanticamente.

'''python
# Ejemplo:
1usuario = "Emersson"
print(1usuario)
'''

Explicación: Este código provocará un error de sintaxis (SyntaxError: invalid decimal literal) antes de que la primera línea pueda ejecutarse. Según las reglas gramaticales de Python, el nombre de una variable nunca puede comenzar con un número. Como rompe la regla de estructura del lenguaje, el intérprete detiene la ejecución de inmediato.


