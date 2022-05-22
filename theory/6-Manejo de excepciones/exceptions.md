# Manejo de excepciones
Manejar los errores puede ir más allá del debugging. Nosotros como programadoras y programadores, podemos decirle al programa
qué hacer cuando ocurran ciertos errores e incluso ocasionarlos intencionalmente.
Para esto hay que conocer una serie de palabras clave: try, except, raise y finally.

## try: probar
Es un bloque de código en el cual se intenta hacer algo, como un input, una sumatoria, etc. Este bloque existe como entorno de 
pruebas controlado, en donde si las cosas salen bien, no saldrá de dicho bloque. Una instrucción try se ve así:
~~~
try:
    numero = int(input("Ingresa un número..."))
~~~

## except: excepto que...
Si sucede algún error en el bloque try, se ejecutará este otro bloque. En este bloque podremos mostrar un mensaje de error, un
re-ingreso de datos o lo que veamos conveniente.
~~~
try:
    numero = int(input("Ingresa un número..."))
except:
    print("Lo que ingresaste no fue un número.")
~~~

Vale, entonces si sucede un error en el bloque try, se ejecutará el bloque except. Eso está cool, pero como sabemos un programa
puede romperse por muchas formas. Desde que se ingresó una cadena en vez de un número, hasta intentar hacer divisiones entre 0.
Entonces, ¿cómo podemos tratar errores de manera individual?

### Tipos de excepciones
Python cubre todos los escenarios donde tu código rompa. Sea cual sea el problema, Python sabrá qué mostrarte en el mensaje de
error para que nos sea más fácil tratar dicho inconveniente. Entre estos tipos de errores, KeyError, ReferenceError, TabError,
RuntimeWarning, SyntaxError, NameError y casos tan específicos como UnicodeEncodeError y BrokenPipeError.

#### ¿Unos son más importantes que otros?
No, pero existe una jerarquía. Se puede decir que hay errores específicos como TabError, los cuales pertenecen a un grupo de 
errores más abstractos como SyntaxError. La lista de errores **nativos de Python** (porque podemos construir los nuestros)
la puedes encontrar en:
[Built-in exceptions](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
\* Ve a la página, te será de ayuda para entender este documento ;)

Y, ¿saber la jerarquía de los errores de qué nos sirve?
Sabiendo esto, podemos estructurar nuestros bloques except, para ejecutar instrucciones de acuerdo a tipos de errores específicos.
~~~
try:
    numero = int(input("Ingresa un número..."))
except UnicodeEncodeError:
    print("Error de codificación del estándar Unicode")
except ValueError:
    print("Lo que ingresaste no fue un número.")
~~~

**NOTA:** Es muy importante recordar que siempre se deben poner los errores más concretos ANTES de los errores generales.
Si por ejemplo ponemos en el primer bloque la excepción _ArithmeticError_ y en el siguiente bloque un error perteneciente a su 
subgrupo, como _ZeroDivisionError_, este último bloque nunca se ejecutará.


## raise: elevar un error
A veces suceden errores que Python no detecta como error, como por ejemplo ingresar una cadena vacía, donde debería haber una 
cadena pero no vacía.
Esto se logra con raise, donde podemos generar un error si se cumple o no una condición, como puede ser si la longitud de la cadena ingresada es igual a 0.
~~~
try:
    cualquier_cosa = input("Ingresa algo...")
    if len(cualquier_cosa) == 0:
        raise ValueError("No se puede ingresar una cadena vacía")
except ValueError as ve:
    print(ve)
~~~
Nótese que le hemos asigndado al error un mensaje y en el bloque except, hemos usado un alias para mejorar la legibilidad y mostrar
ese mensaje de error asignado a la excepción.

## finally: finalizar
Se usa al final de una estructura try-except para poder cerrar un archivo, cerrar una conexión a una base de datos o liberar 
recursos externos. No es muy frecuente su uso.
~~~
try:
    f = open('archivo.txt')
    # hace cualquier cosa con nuestro archivo
finally:
    f.close()
~~~
En este ejemplo de código, se abre un archivo e independientemente de si sucede un error o no, se cierra el archivo.

## assert: afirmación
Asserts es una expresión en Python que también podemos usar para tratar errores. Su flujo es el siguiente:
Tenemos dentro del código un assert (que es una afirmación). Si esta afirmación se cumple (assert retorna True), el código sigue
su flujo. Pero si no se cumple (assert retorna False), devolvemos un error.
Su estructura es la siguiente:
'assert condición, mensaje de error'
Veámos un ejemplo:
~~~
cualquier_cosa = input("Ingresa algo...")
assert len(cualquier_cosa) > 0, "No se puede ingresar una cadena vacía"
~~~
Básicamente, si una afirmación es cierta el programa continúa. Pero de ser falsa, el programa se detiene y muestra el valor que le 
indiquemos.
