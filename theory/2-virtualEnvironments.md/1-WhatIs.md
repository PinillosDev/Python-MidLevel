### Módulos
Antes, mejor recordar el concepto de módulos
Un módulo es código escrito por otra persona que nos sirve para resolver nuestro problema. Es código que usamos
para no re-inventar la rueda. Ese módulo lo podemos 'importar' en nuestro programa y usarlo.

# Problemas ancestrales
Cuando se instala Python, lo solemos hacer con una versión determinada como puede ser 3.10.
Esto puede ser un problema, porque si queremos trabajar con módulos, librerías o _frameworks_ que funcionan
con una versión específica de Python, tendremos problemas de compatibilidad. Ahora imagina el problema cuando se
necesitaba compartir el código con otra persona.

# ¿Qué es un entorno virtual?
Un entorno virtual es la solución perfecta a este problema.
Es como una caja, donde puedes tener diferentes versiones de Python en cada una y donde puedes instalar diferentes
módulos para tener proyectos aislados.
Básicamente en un entorno virtual tienes una versión de Python, compatible con lo que necesites instalar para
realizar un proyecto en específico.

## Entorno virtual en Linux
\* UBUNTU 20.04:
Para crear un entorno virtual, primero se debe habilitar **ensurepip**
Se ejecuta en consola en cualquier directorio:
'sudo apt install python3.8-venv'

Para crear un entorno virtual, se ejecuta en consola en la carpeta de tu proyecto:
'python3 -m venv venv'

Veamos esta intrucción más de cerca:
- python3 -> comando para usar las funciones de Python
- -m -> llamar un módulo
- venv -> virtual enviorment, este es el módulo que se llamará
- venv -> el nombre que le vamos a poner, por convención es el mismo (venv)

Para activar el entorno virtual se hace
'source venv/bin/activate_'
Para desactivar se usa _deactivate_

## Entorno virtual en Windows
'python -m venv venv # Crea el entorno virtual'
'.\venv\Scripts\activate # Activa el entorno virtual'
