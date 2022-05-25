# PIP
PIP (Package Installer for Python) es un módulo que nos permitirá instalar módulos, librerías o frameworks
que no vienen incluidos con Python.

## Linux
\* Ubuntu 20.04
Para instalar pip, hacemos
'sudo apt install python3-pip'

Para ver los paquetes que tenemos instalados, hacemos
'pip freeze'

Para instalar un módulo, basta con
'pip install <modulo>'

Ahora, necesitamos que las personas con las que vamos a compartir el código tengan los mismos paquetes instalados
con las mismas versiones. Para esto, creamos un archivo de texto donde se almacenen los nombres y versiones de los
paquetes con los que estamos trabajando.
'pip freeze > requirements.txt'

\* En Linux, el operador _>_ sirve para guardar el resultado de un comando (en este caso pip freeze en el archivo que
va después de ese operador.
Lo que se logra con esto es guardar en un txt todos los módulos y las versiones de nuestro proyecto.

Para que la persona que va a trabajar con nuestro proyecto se baje todos los requerimientos, se ejecuta en consola
'pip install -r requirements.txt'
Con esto, se le instalará todo en su entorno virtual.

## Windows
Sinceramente te recomiendo que instales Anaconda, que es una distribución de Python muy completa, que incluye pip y
más herramientas como Spyder (un IDE muy epic) y Jupyter (una especie de notebook para ciencia de datos). It's free.
![Anaconda](https://www.anaconda.com/products/distribution)

Con anaconda, puedes usar el _Anaconda Prompt_, una consola donde puedes usar los siguientes comandos:
'conda create --name djangoProject python=3.8'
Este comando crea un entorno virtual llamado djangoProject, usando la versión de Python 3.8
Para installar modulos, se hace
'conda install django'
