
from persona import Persona
from deportista import Deportista


class Futbolista(Persona, Deportista):

    listaFutbolistas = []

    def __init__(self, nomb, edad, alt, sex, ap,  gm, tr, ph):
        self._golesMarcados = gm
        self._tarjetasRojas = tr
        self._piernaHabil = ph
        Persona.__init__(self, nomb, edad, alt, sex)
        Deportista.__init__(self, "Futbol", ap)
        Futbolista.listaFutbolistas.append(self)

    def setGolesMarcados(self, gm):
        self._golesMarcados = gm

    def setTarjetasRojas(self, tr):
        self._tarjetasRojas = tr    

    def setPiernaHabil(self, ph):
        self._piernaHabil = ph

    def getGolesMarcados(self):
        return self._golesMarcados
    
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    
    def getPiernaHabil(self):
        return self._piernaHabil
    
    def __str__(self):
        txt = f"Mi nombre es {Persona.getNombre(self)} soy profesional en el deporte {Deportista.getDeporte(self)} Tengo {Persona.getEdad(self)} años de edad y llevo {Deportista.getAñosPracticando(self)} años en el deporte"
        return txt
