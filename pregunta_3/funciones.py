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
