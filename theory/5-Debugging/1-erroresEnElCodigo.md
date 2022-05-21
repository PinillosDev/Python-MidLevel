# Los errores en el código

Es completamente normal tener errores en nuestro código. Contrario a lo que se puede esperar, los errores nos sirven para saber 
qué está mal y arreglarlo antes de que salga a producción. Los errores son tan comúnes y útiles, que deberían ser el mejor amigo
de todo programadora y programador.

## ¿Cómo Python ejecuta nuestro código?
Para entender los errores, primero debemos saber cómo Python ejecuta nuestro código. Antes de ejecutar nuestro código, el
intérprete va línea por línea verificando que el código sea correcto sintácticamente. Es decir, que los nombres de las variables
sean correctos, que no se hagan operaciones entre *int* y *str*, que no se estén usando palabras reservadas para nombrar funciones,
entre otros casos.

Si el intérprete encuentra un error, para automáticamente y nos muestra un error como este:
1) qué tipo de error (ejemplo: SyntaxError)
2) Dónde ocurrió (Ejemplo: line 13)
3) En qué módulo ocurrió (ejemplo: main())

Pero hay un problema: los errores de los que nos avisa el intérprete de Python son errores sintácticos, de valor, de división entre
cero, índices fuera de valor, llaves que no existen, entre otros.

¿Qué sucede cuando nuestro código está bien escrito, pero aún así las cosas *no salen como deberían*?
¿Cómo se tratan los errores de lógica?
