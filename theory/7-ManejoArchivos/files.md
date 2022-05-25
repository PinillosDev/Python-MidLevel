# Manejo de archivos con Python
Existen dos grandes tipos de archivos

## Los de texto plano
Donde su contenido son bits que significan un carácter, letra, número, etc. Entre ellos están .csv, .txt, .py, .html, etc.
Estos son archivos de texto plano, no hay tipos de fuente, no hay carácteres, no hay márgenes; solo texto.
Por ejemplo este archivo es de texto plano.

## Los binarios
Donde su contenido lo constituye código binario, por lo que su contenido no puede ser leído mediante un editor de código como VS 
Code.
¿Alguna vez has intentado abrir un archivo de Word en un editor de código? Si lo haces, vas a ver que su contenido son un montón de
carácteres extraños. Esto es porque los archivos binarios no son de texto plano, se necesitan programas especiales para visualizarlos.
Ejemplos de archivos binarios tenemos a .mp4, .mkv, .jpg, .mp3, etc.

# Al grano...
Para abrir un archivo de texto con Python podemos usar tres formas:
### R -> Lectura: Para ver lo que tiene este archivo por dentro.
### W -> Escritura: Para poder escribir desde cero un archivo (sobreescribir)
### A -> Escritura: Para agregar un contenido al final.

## ¿Cómo se trabaja con un archivo?
Antes de entrar de lleno, hay que memorizarse esta línea de código:

'with open("<file_path>", "r") as file:'

En esta línea hay nuevas palabras reservadas:
- with
Es un manejador contextual. Lo que hace es controlar el flujo de nuestro archivo haciendo que si se cierra el programa o el 
Script finaliza inesperadamente, el archivo no se rompa.

- open()
Es una función que abre archivos en Python y lleva dos parámetros. El directorio del archivo y el modo de apertura (r, w, a)

- as
Significa alias y después del _as_, le asignamos un nomobre al archivo con el que lo podremos llamar más adelante.
Veamos un ejemplo real de cómo manejar un archivo con Python.

~~~
with open("archivos/numbers.txt", "r", encoding="utf-8") as file:
    print(file.read())
~~~
### Más palabras reservadas...
- encoding="utf-8"
Evita errores cuando estamos trabajando con carácteres especiales (tildes, letras de otros idiomas, etc.)
- file.read()
read() es un método de archivos, el cual nos permite mostrar el contenido que este tiene.