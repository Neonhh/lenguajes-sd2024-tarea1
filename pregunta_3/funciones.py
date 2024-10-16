#variables globales
#Guardaremos los programas, interpretes y traductores en sets para que no se repitan
interpretes = {}
traductores = {}
#los programas se guardan en un diccionario, donde la llave es el nombre del programa
#y el valor es el lenguaje en que esta escrito
programas = {}
#Y tambien guardaremos en un set los lenguajes que se pueden interpretar desde LOCAL
lenguajes = {'LOCAL'}

#Definiciones de funciones

#Dado que se va a definir un nuevo programa, determina el tipo de programa
#y llama a la funcion correspondiente o imprime un mensaje de error
def definir(instruccion):
    tipo = instruccion[0]

    if tipo == 'PROGRAMA':
        return programa(instruccion[1], instruccion[2])
    elif tipo == 'INTERPRETE':
        return interprete(instruccion[1], instruccion[2])
    elif tipo == 'TRADUCTOR':
        return traductor(instruccion[1], instruccion[2], instruccion[3])
    else:
        print("Error en los argumentos.")
        print("Opciones:\n DEFINIR PROGRAMA <nombre> <lenguaje>")
        print(" DEFINIR INTERPRETE <lenguaje_base> <lenguaje>")
        print(" DEFINIR TRADUCTOR <lenguaje_base> <lenguaje_origen> <lenguaje_destino>")

#Revisa si un programa definido es ejecutable en LOCAL
def ejecutable(nombre):
    
    lenguaje = programas.get(nombre)
    if lenguaje == None:
        print("Programa no definido.")
    elif lenguaje in lenguajes:
        print("Si, es posible ejecutar el programa '" + nombre + "'.")
    else:
        print("No es posible ejecutar el programa '" + nombre + "'.")

#define un nuevo programa en el lenguaje especificado
#Nota: Si el programa ya esta definido, la definicion anterior se sobreescribe
def programa(nombre, lenguaje):
    if nombre in programas:
        print("El programa '" + nombre + "' ya esta definido.")
        return

    programas.update({nombre: lenguaje})
    print("Se definio el programa '" + nombre + "', ejecutable en '" + lenguaje + "'.")    

#Define un interprete para lenguaje escrito en lenguaje_base
def interprete(lenguaje_base, lenguaje):

    #Primero, queremos ver si este interprete nos permite ejecutar programas
    #de este lenguaje
    if lenguaje_base in lenguajes:
        lenguajes.add(lenguaje)

        #Si lo permite, entonces tambien permite correr los interpretes
        #que tengan a este como lenguaje_base
        lenguajes_interpretados = interpretes.get(lenguaje)
        if lenguajes_interpretados != None:
            for interpretado in lenguajes_interpretados:
                lenguajes.add(interpretado)
            
            interpretes.pop(lenguaje)
        #Si no hay mas lenguajes interpretados, no hacer nada
    else:
        #Si no, queremos ver si ya hay un interprete escrito en lenguaje_base
        lenguajes_interpretados = interpretes.get(lenguaje_base)

        #Si no lo hay, define una nuevo. Si lo hay, agregale este lenguaje
        if lenguajes_interpretados == None:
            interpretes.update({lenguaje_base: {lenguaje}})
        else:
            lenguajes_interpretados.add(lenguaje)
            interpretes.update({lenguaje_base: lenguajes_interpretados})
    
    print("Se definió un intérprete de '"+ lenguaje + "' escrito en '" + lenguaje_base + "'.")
        
