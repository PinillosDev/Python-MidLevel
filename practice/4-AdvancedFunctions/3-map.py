if __name__ == "__main__":
    myList = [number for number in range(1, 51)] # Crea una lista de enteros de 1 a 50
    print(f"\nLista sin filtrado -> {myList}\n")
    newList = list(map(lambda x: x*2, myList))
    print(f"\nLista filtrada -> {newList}\n")
