def read_file():
    print("Contenido en el archivo:\n")
    with open("nombres.txt", "r", encoding="utf-8") as file: # Se abre el archivo a modo de lectura
        for line in file:
            print(line) # Se muestra nombre a nombre
    return print("\n\nArchivo leído con éxito")


def write_file():
    nombres = ['Juan', 'Fredy', 'Vitalik', 'Satoshi', 'Angela']
    with open("nombres.txt", "w", encoding="utf-8") as file: # Se abre el archivo a modo de escritura
        for name in nombres:
            file.write(name) # Se escriben los nombres desde la lista nombres
            file.write("\n") # Se añade un salto de línea
    return print("Archivo sobre escrito con éxito")


def main():
    write_file()
    read_file()


if __name__ == "__main__":
    main()