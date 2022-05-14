# High order functions o *funciones de orden superior*
Una función de orden superior es una función que recibe como parámetro otra función. En todos los lenguajes de programación, 
existen tres que son muy populares y útiles.

- FILTER
Esta _high order funtion_ nos sirve para filtrar un iterable. Puede ser para eliminar de una lista strings con cierta letra,
quitar de un diccionario las tuplas vacías, etc. Es una función muy útil.
Por ejemplo, tenemos una lista con números aleatorios y queremos obtener solo los números impares, esta función nos sería muy
útil.
La función filter recibe dos parámetros: una función (como una lambda) y un iterable.


- MAP
Con esta función hacemos operaciones sobre un iterable para generar otro iterable. A diferencia de filter, nos interesa filtrar y
guardar nuestros datos _filtrados_ en otra variable.
Básicamente con él hacemos una operación sobre un iterable para generar otro iterable.
Otro interesante uso es que podemos usar condicionales en la expresión *lambda* y nuestra lista resultado se llenará de
_True_ o _False_, dependiendo de si nuestros elementos en la lista original cumplen o no con la condición.


- REDUCE
Reduce nos es útil cuando queremos reducir una variable a una sola expresión. 
Por ejemplo, tenemos una lista de números enteros y queremos que se reduzcan a una sola expresión; ya sea sumándolos, restándolos,
etc. A diferencia de las funciones anteriores, hay que importar la librería reduce.