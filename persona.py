class Persona:
    def __init__(self, nombre, edad, altura, sexo):
        self._nombre = nombre
        self._edad = edad
        self._altura = altura
        self._sexo = sexo

    def setNombre(self, nomb):
        self._nombre = nomb

    def setEdad(self, edad):
        self._nombre = edad

    def setAltura(self, alt):
        self._nombre = alt

    def setSexo(self, sexo):
        self._nombre = sexo

    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad
    
    def getAltura(self):
        return self._altura
    
    def getSexo(self):
        return self._sexo
