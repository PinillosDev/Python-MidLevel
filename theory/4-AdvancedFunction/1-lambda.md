# Funciones lambda
Las funciones anónimas (o lambda) son funciones que tienen una serie de características diferentes a las funciones comúnes.

A pesar de que las funciones Lambda puedan tener los parámetros que nosotros consideremos necesarios, su principal carácterística 
es que solo puede tener una línea de código y una sola expresión. Por ejemplo, veamos la siguiente función:

_def operation(number):_
    _return number * 2_

Ahora veamos esta misma función pero en *versión Lambda*

_operation = lambda number: number*2_

# Veámos por partes:
- operation -> identificador, vendría a ser el nombre de la función

- lambda -> indica que es una función anónima (lambda)

- number -> es el argumento que se tomará

- : -> Se debe poner, es la ley y diferencia el parámetro de la expresión

- number*2 -> Es la operación que se reliazará con el parámetro

____________________________________________________________________

Si las funciones lambda no tienen nombre, ¿cómo se van a a llamar?
Si bien las lambda no tienen un identificador, se llaman con el nombre de la variable donde se va a guardar el resultado. En este 
caso, operation.