nombre = "emerson"
print(isinstance(nombre, str))

edad = 15
print(isinstance(edad,int))


decimal = 5.0
print(isinstance(decimal, float))


booleano = True
print(isinstance(booleano,bool))


if edad.is_integer():
    print("Efectivamente es un numero!")


lista = [1,2,3,4,5]
print(type(lista))

tupla = (1,2,3,4,5,6)
print(type(tupla))


diccionario = {
    "manzana": 2,
    "pera":0,
    "mandarina": 5
}
print(type(diccionario))
