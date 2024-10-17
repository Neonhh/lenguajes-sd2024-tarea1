#estos modulos estan definidos en el directorio 'pregunta_3'
#from estructuras import *
from funciones import *

#Cuerpo principal
def main():
    continuar = True
    #Prompt inicial
    print("Iniciando ejecucion del programa simuladorT.")
    print("Opciones:\n DEFINIR <tipo> [<argumentos>]")
    print(" EJECUTABLE <programa>\n SALIR\n")

    #Seleccion de opciones
    while continuar:

        print("$> ", end="")
        comando = input()

        #Si se ingresa 'SALIR', solo hay que salirse.
        if comando == 'SALIR':
            continuar = False
    
        #En caso contrario, hay que dividir la instruccion.
        else:
            instruccion = comando.split()
            if instruccion[0] == 'DEFINIR':
                definir(instruccion[1:])
            elif instruccion[0] == 'EJECUTABLE':
                ejecutable(instruccion[1])
            else:
                print("Comando no reconocido.")
                print("Opciones:\n DEFINIR <tipo> [<argumentos>]")
                print(" EJECUTABLE <programa>\n SALIR\n")

if __name__ == "__main__":
    main()
            