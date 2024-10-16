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
