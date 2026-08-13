    # Tema: Variables y Tipos de Datos
**Fecha:** 2026-08-11

## Método de Aprendizaje
Este apartado de notas busca hacer el ejercicio de pensar realmente el concepto y explicarlo con mis propias palabras, no solo copiar y pegar texto sin finalidad.

---

## 1. Variables
Una **variable** es un espacio en memoria que se reserva para guardar diferentes tipos de datos bajo un nombre que la identifica. Es uno de los conceptos más importantes dentro de la programación, ya que permite almacenar, reutilizar y manipular información a lo largo de la ejecución de un programa.

---

## 2. Tipos de Datos
En programación, los tipos de datos indican la naturaleza de la información que se va a procesar. Se dividen principalmente en dos grandes categorías:

### A. Datos Primitivos
Son los datos más básicos de un lenguaje. Tienen una naturaleza inherente y propia, lo que significa que no son la combinación o agrupación de otros tipos de datos.

#### Ejemplos en Python:

```python
# Entero (int): Números enteros sin parte decimal
edad = 18  # type(int)

# Cadena de texto (str): Texto o secuencia de caracteres
nombre = "Emersson"  # type(str)

# Booleano (bool): Estado lógico de verdadero o falso
es_hombre = True  # type(bool)

# Flotante (float): Números con representación decimal
nota = 4.0  # type(float)

# Ausencia de valor (NoneType): Representa un valor nulo o vacío
valor_vacio = None  # La 'N' inicial siempre debe ir en mayúscula
```

#### Comportamiento especial en Python frente a otros lenguajes
A diferencia de lenguajes como C, C++ o Java, donde los tipos primitivos guardan valores "puros" o crudos directamente en la memoria RAM, **en Python todo es un objeto**. 

Cuando se declara `edad = 18`, Python no guarda un simple número entero aislado; crea un objeto completo en memoria perteneciente a la clase `int` que contiene el valor, su dirección de memoria, el contador de referencias y sus métodos internos.

---

### B. Datos Compuestos (No Primitivos)
Son tipos de datos construidos a partir de la combinación o agrupación de datos primitivos. Permiten almacenar y organizar colecciones de información bajo una misma estructura.

#### Principales estructuras en Python:
* **Listas (`list`):** Colección ordenada y modificable (mutable). Ejemplo: `[1, 2, 3]`
* **Tuplas (`tuple`):** Colección ordenada pero inalterable (inmutable). Ejemplo: `(10, 20)`
* **Diccionarios (`dict`):** Estructura organizada en pares clave-valor. Ejemplo: `{"nombre": "Emersson", "edad": 18}`
* **Conjuntos (`set`):** Colección no ordenada de elementos únicos sin duplicados. Ejemplo: `{1, 2, 3}`