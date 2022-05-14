if __name__ == "__main__":
    myList = [number for number in range(1, 51)] # Crea una lista de enteros de 1 a 50
    print(f"\nLista sin filtrado -> {myList}\n")
    myList = list(filter(lambda x: x%2 == 0, myList))
    print(f"\nLista filtrada -> {myList}\n")

"""
En la línea 4 -> lambda x: x%2 == 0
Esta es la función, el primer parámetro de filter. x es cada elemento del segundo parámetro de la función filter (myList).
como expresión de la función lambda, tenemos una operación ya conocida, x%2 == 0; usada para validar si un número es par.
"""