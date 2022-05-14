from functools import reduce

if __name__ == "__main__":
    myList = [number for number in range(1, 11)]
    print(f"\nLista antes del filtrado -> {myList}")
    myList = reduce(lambda a, b: a*b, myList)
    print(f"Lista filtrada -> {myList}\n")


"""
En la línea 6, tenemos una función lambda que usa como parámetros dos variables (a, b). En la primera iteración:
a = myList[0]
b = myList[1]

En la expresión, se nos muestra a*b. Es decir, el primer elemento (a) del iterable (myList) se multiplica con el segundo (b).

En la siguiente iteración:
a = myList[0] * myList[1]
b = myList[2]
Y así sucesivamente.

Básicamente, se tiene [4, 6, 2, 2]
a * b = 4 * 6 = 24
a * b = 24 * 2 = 48
"""