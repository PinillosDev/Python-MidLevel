Antes, mejor recordar el concepto de módulos:
Un módulo es código escrito por otra persona que nos sirve para resolver nuestro problema.
Es código que usamos para no re-inventar la rueda.
Ese módulo lo podemos 'importar' en nuestro programa y usarlo.

# ¿Qué es un entorno virtual?
Es como una caja, donde puedes tener diferentes versiones de Python y donde puedes instalar diferentes módulos para tener proyectos aislados.
Los entornos se crearon porque al trabajar sobre varios proyectos en el mismo computador, significa enfrentarse a problemas de compatibilidad. Incompatibilidad con nuestra versión de Python y módulos, por ejemplo.
Uno caso de ejemplo es que tengamos la versión 3.6 de Python, pero para trabajar en otro proyecto necesitamos otra versión, ya que los módulos que necesitamos solo funcionan con esa versión específica de Python.

Es por esto que lo mejor es tener una caja donde tenemos una versión de Python y allí instalar paquetes que requieren esa versión
específica de Python. Y así con cada proyecto, tener todo lo necesario para un proyecto en nuestra _caja_.

# Instalación UBUNTU 20.04:
Para crear un entorno virtual, primero se debe habilitar *ensurepip*
Se ejecuta en consola en cualquier directorio:
_sudo apt install python3.8-venv_


Para crear un entorno virtual, se ejecuta en consola en la carpeta de tu proyecto:
_python3 -m venv venv_

Veamos esta intrucción más de cerca:
python3 -> comando para usar las funciones de Python
-m -> llamar un módulo
venv -> virtual enviorment, este es el módulo que se llamará
venv -> el nombre que le vamos a poner, por convención es el mismo (venv)

Para activar el entorno virtual se hace
_source venv/bin/activate_
Para desactivar se hace _deactivate_