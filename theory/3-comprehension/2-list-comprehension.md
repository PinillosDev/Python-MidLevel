# List comprehension
Cuando queremos crear una lista, podemos hacerlo de varias formas. Hoy aprenderemos a hacerlo de una manera r�pida
y sencilla.
List comprehension o comprensi�n de listas es crear una lista con x valores e incluso con condiciones en una
�nica l�nea.

Sigue la siguiente estructura.


_odd = [element for element in range(1, 11)]_
  |        |                |
lista      |                |
           |                |
    Elemento con que        |
    se llenar� la lista     |
                            |

                for element in range(1, 11)
        Aqu� se indica que por cada valor de element
        (1 en la primera iteraci�n, 2 en la segunda, etc)
        se agregar� ese valor a la lista


Ahora, si se quiere agregar una condici�n, por ejemplo que solo se agreguen los elementos si son par, se hace
'odd = [element for element in range(1, 11) if element%2 == 0]'