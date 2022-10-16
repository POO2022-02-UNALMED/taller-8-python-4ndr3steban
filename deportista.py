class Deportista:
    def __init__(self, deporte, anosprac):
        self._deporte = deporte
        self._añosPracticando = anosprac

    def setDeporte(self, dep):
        self._deporte = dep

    def setAñosPracticando(self, ap):
        self._añosPracticando = ap

    def getDeporte(self):
        return self._deporte

    def getAñosPracticando(self):
        return self._añosPracticando