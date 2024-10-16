#Definiciones de estructuras de datos
class interprete:
    def __init__(self, escritoEn, *para):
        self.escritoEn = escritoEn
        self.para = set(para)

    #definimos __eq__ y __hash__ para poder guardar estos en un set.
    def __eq__(self, other):
        if not isinstance(other, interprete):
            return False
        #Solo me interesa escritoEn, porque todos los lenguajes para el que
        #esta escrito se guardaran en la misma estructura.
        return self.escritoEn == other.escritoEn
        
    def __hash__(self):
        return hash(self.escritoEn)
  

class traductor:
    def __init__(self, escritoEn):
        self.escritoEn = escritoEn
        
        #Esto sera una abstraccion, y se guardara como un set de interpretes,
        #Porque, como solo queremos saber si un programa es ejecutable,
        #Podemos verlo como que si puedo interpretar el lenguaje en que esta
        #escrito el traductor de A a B, es lo mismo que tener un interprete
        #para A escrito en B.
        self.traduce = {}

    #Igualmente los traductores se guardaran en un set
    #definimos __eq__ y __hash__ para poder guardar estos en un set.
    def __eq__(self, other):
        if not isinstance(other, traductor):
            return False
        #Solo me interesa escritoEn, porque todos los lenguajes para el que
        #esta escrito se guardaran en la misma estructura.
        return self.escritoEn == other.escritoEn
        
    def __hash__(self):
        return hash(self.escritoEn)

#A estas alturas, que tanto danho mas hace tener una clase tambien para programas?
class programa:
    def __init__(self, escritoEn, nombre):
        self.escritoEn = escritoEn
        self.nombre = nombre

    def __eq__(self, other):
        if not isinstance(other, programa):
            return False
        return self.escritoEn == other.escritoEn and self.nombre == other.nombre

    def __hash__(self):
        return hash((self.escritoEn, self.nombre))

#Definiciones de funciones
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

def ejecutable(instruccion):
    pass



#Guardaremos los programas, interpretes y traductores en sets para que no se repitan
programas = {}
interpretes = {}
traductores = {}

#Cuerpo principal
continuar = True
#Prompt inicial
print("Iniciando ejecucion del programa simuladorT.")
print("Opciones:\n  DEFINIR <tipo> [<argumentos>]")
print("EJECUTABLE <programa>\n SALIR\n")

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
            ejecutable(instruccion[1:])
        else:
            print("Comando no reconocido.")
            print("Opciones:\n  DEFINIR <tipo> [<argumentos>]")
            print("EJECUTABLE <programa>\n SALIR\n")


            