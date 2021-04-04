# Esto se un comenaio de python 3
if 6 > 5:
    print('6 es mayor a 5')

x = 5
y = 'Hola'
# otro mernsaje

# print(x, y)

email = 'yeisondesing@gmail.com'

# print(email)

# Manejo de listaas 
lista = [1, 2, 3, 1, 2, 2]
lista2 = lista.copy()
lista.append(4)
# lista.clear()  Esto limpia la listaa
# print(lista, lista2.count(2))
# print(len(lista), len(lista2))

listaWords = ['Hola', 'Mundo', 'Soy un Gordito']
# print(listaWords[2])

# Eliminar elementos 
# lista.pop() Solo elimina el último elemento
#  elimina por elemento 
# listaWords.remove('Hola')
# print(listaWords)


# lista.reverse() revierte el orden de la listaa 
lista.sort()
listaWords.sort()
listaWords.reverse()
# print(lista, listaWords)

# crear tuplas
tupla = ('Hola', 'Mundo', 'Somos', 'Tupla')
# print(tupla.index('Mundo'))

# transformamos tupla a listaa
listaDeTupla = list(tupla)
# print(listaDeTupla)

# rangos 
rango = range(6)
# print(rango)

# diccionarios, se usan strings para encontrar un valos en particular
# Esto es un puto array
diccionario = {
    'nombre': 'Simón',
    'raza': 'Criollo',
    'edad': 6
}

# print(diccionario)
# print(diccionario['nombre'])
# print(diccionario['raza'])
# print(diccionario.get('raza'))
# cambiar valores 
diccionario['nombre'] = 'Raúl'
# print(diccionario['nombre'])
# print(len(diccionario))

diccionario['ronronea'] = 'si'
print(diccionario)

# se elimina con pop o poo item (Este último elimina el útimo valor) o del
# diccionario.pop('ronronea')
# diccionario.popitem()
del diccionario['ronronea']
print(diccionario)

# Eliminar todos los elementos 
diccionario.clear()
print(diccionario)


