# Pregunta 3 - simulador de traductores (simuladorT)

en esta carpeta se encuentran los archivos necesarios para correr el codigo. El programa principal es `simuladorT.py`, que importa `funciones.py`.

Se realizaron los tests unitarios y de cobertura, alcanzando una cobertura de 92%. Los test escritos (asistidos por IA) y el index.html con los resultados se encuentran en la carpeta `lenguajes-sd2024-tarea1/tests`.

## Ejecucion del programa

Teniendo python instalado, en el directorio donde se encuentran `simuladorT.py` y `funciones.py`ejecutar el comando `python -u simuladorT.py`.

Esto empezara la ejecucion del programa, presentando un resumen de los comandos posibles.

## Ejecucion de las pruebas

En la carpeta `lenguajes-sd2024-tarea1/tests` se encuentra el archivo con los resultados de las pruebas. Para reproducirlas, se puede utilizar pytest junto con coverage. Para esto, colocarse en repositorio padre de `test` y `pregunta_3` (deben estar ambos en el mismo directorio) y ejecutar `coverage run -m pytest tests`. Para ver los resultados en el terminal se usa el comando `coverage report` y para generar el archivo index.html con los resultados se usa `coverage html`.