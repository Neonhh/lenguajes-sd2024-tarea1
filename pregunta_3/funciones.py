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
        interprete(instruccion[1], instruccion[2])
        print("Se definió un intérprete de '"+ instruccion[1] + "' escrito en '" + instruccion[2] + "'.")
    elif tipo == 'TRADUCTOR':
        traductor(instruccion[1], instruccion[2], instruccion[3])
        print("Se definió un traductor de '"+ instruccion[2] + "' hacia '" + instruccion[3] + "' escrito en '" + instruccion[1] + "'.")
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
        agregar_lenguaje(lenguaje)
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

#Define un traductor escrito en lenguaje_base, de lenguaje_origen a lenguaje_destino
def traductor(lenguaje_base, lenguaje_origen, lenguaje_destino):
    
    #Primero vemos si podemos ejecutar lenguaje_base
    if lenguaje_base in lenguajes:
        #De ser asi, podemos abstraernos y pensar en el traductor como un interprete
        #para lenguaje_origen escrito en lenguaje_destino
        interprete(lenguaje_destino, lenguaje_origen)

    else:
        #Si no, almacenamos el traductor por si el lenguaje_base se agrega luego
        traducciones = traductores.get(lenguaje_base)

        if traducciones == None:
            traductores.update({lenguaje_base: {lenguaje_origen: lenguaje_destino}})
        else:
            traducciones.add({lenguaje_origen: lenguaje_destino})
            traductores.update({lenguaje_base: traducciones})

#Maneja las operaciones a considerar cuando se agrega un lenguaje ejecutable
# esta funcion se define recursivamente para que se puedan agregar lenguajes
# en cadena siempre que existan los interpretes (o traductores)
# Es muy probable que esto hubiera podido hacerse con un DSU... peeero ya no hice eso desde el principio, asi que en lugar de eso tenemos un misterio.
def agregar_lenguaje(lenguaje):
    lenguajes.add(lenguaje)

    #Si lo permite, entonces tambien permite correr los interpretes
    #que tengan a este como lenguaje_base
    lenguajes_interpretados = interpretes.get(lenguaje)
    if lenguajes_interpretados != None:
        for interpretado in lenguajes_interpretados:
            agregar_lenguaje(interpretado)
            
        interpretes.pop(lenguaje)
    
    #Tambien hay que considerar los traductores escritos en el lenguaje
    traducciones = traductores.get(lenguaje)
    if traducciones != None:
        for lenguaje_origen in traducciones: #iterar sobre diccionarios devuelve solo el key
            lenguaje_destino = traducciones.get(lenguaje_origen)
            #Si el lenguaje destino es ejecutable, agrega el lenguaje origen como ejecutable
            if(lenguaje_destino in lenguajes):
                agregar_lenguaje(lenguaje_origen)
            else:
                #Si no, a partir de ahora tratalo como un interprete:
                interprete(lenguaje_destino, lenguaje_origen)

        traductores.pop(lenguaje)